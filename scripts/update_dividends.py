#!/usr/bin/env python3
"""
scripts/update_dividends.py

Offline cron script to fetch latest dividend distribution data for JEIP and JEQP
from Yahoo Finance and update market/index.html automatically.
Zero external dependencies (uses standard library urllib and json).
"""

import datetime
import json
import os
import re
import urllib.request


def fetch_fund_data(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1y&events=div"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    
    result = payload["chart"]["result"][0]
    meta = result["meta"]
    price = meta.get("regularMarketPrice", 0)
    currency = meta.get("currency", "GBp")

    raw_divs = result.get("events", {}).get("dividends", {})
    # Sort dividends by timestamp descending
    div_list = sorted(raw_divs.values(), key=lambda x: x["date"], reverse=True)

    # Calculate trailing 12-month (365 days) total dividends
    now_ts = datetime.datetime.now(datetime.timezone.utc).timestamp()
    ttm_divs = [d["amount"] for d in div_list if (now_ts - d["date"]) <= 365 * 86400]
    ttm_total = sum(ttm_divs)
    yield_pct = (ttm_total / price * 100) if price else 0

    formatted_divs = []
    for d in div_list[:5]:
        ex_dt = datetime.datetime.fromtimestamp(d["date"], datetime.timezone.utc)
        # Payment date is usually the first Wednesday/Friday of the subsequent month (~25-28 days later)
        # Approximate pay date: ex_date + 27 days
        pay_dt = ex_dt + datetime.timedelta(days=27)
        formatted_divs.append({
            "ex_date": ex_dt.strftime("%Y-%m-%d"),
            "pay_date": pay_dt.strftime("%Y-%m-%d"),
            "amount": d["amount"],
            "month_str": ex_dt.strftime("%b %Y"),
        })

    return {
        "ticker": ticker,
        "price": price,
        "currency": currency,
        "yield_pct": yield_pct,
        "latest": formatted_divs[0] if formatted_divs else None,
        "history": formatted_divs,
    }


def build_table_rows(div_history, unit="p"):
    rows = []
    for item in div_history[:4]:
        amount_str = f"{item['amount']:.2f} {unit}"
        rows.append(
            f"                            <tr>\n"
            f"                                <td>{item['ex_date']}</td>\n"
            f"                                <td>{item['pay_date']}</td>\n"
            f"                                <td class=\"amount-col\">{amount_str}</td>\n"
            f"                            </tr>"
        )
    return "\n".join(rows)


def replace_marker(content, marker_name, new_value):
    pattern = rf"(<!-- {marker_name} -->)(.*?)(<!-- /{marker_name} -->)"
    replacement = rf"\g<1>{new_value}\g<3>"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def main():
    print("Fetching dividend data from Yahoo Finance...")
    jeip = fetch_fund_data("JEIP.L")
    jeqp = fetch_fund_data("JEQP.L")

    print(f"JEIP: Price={jeip['price']} GBp, Yield={jeip['yield_pct']:.2f}%, Latest={jeip['latest']}")
    print(f"JEQP: Price={jeqp['price']} GBp, Yield={jeqp['yield_pct']:.2f}%, Latest={jeqp['latest']}")

    html_path = os.path.join(os.path.dirname(__file__), "..", "market", "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update JEIP
    jeip_yield_str = f"~{jeip['yield_pct']:.1f}%"
    jeip_latest_amt = f"{jeip['latest']['amount']:.2f} <span style=\"font-size:0.8rem;font-weight:600;\">p</span>"
    jeip_latest_sub = f"{jeip['latest']['month_str']} 派息"
    jeip_table_html = build_table_rows(jeip["history"], unit="p")

    content = replace_marker(content, "JEIP_YIELD", jeip_yield_str)
    content = replace_marker(content, "JEIP_LATEST", jeip_latest_amt)
    content = replace_marker(content, "JEIP_LATEST_SUB", jeip_latest_sub)
    content = replace_marker(content, "JEIP_TABLE", jeip_table_html)

    # Update JEQP
    jeqp_yield_str = f"~{jeqp['yield_pct']:.1f}%"
    jeqp_latest_amt = f"{jeqp['latest']['amount']:.2f} <span style=\"font-size:0.8rem;font-weight:600;\">p</span>"
    jeqp_latest_sub = f"{jeqp['latest']['month_str']} 派息"
    jeqp_table_html = build_table_rows(jeqp["history"], unit="p")

    content = replace_marker(content, "JEQP_YIELD", jeqp_yield_str)
    content = replace_marker(content, "JEQP_LATEST", jeqp_latest_amt)
    content = replace_marker(content, "JEQP_LATEST_SUB", jeqp_latest_sub)
    content = replace_marker(content, "JEQP_TABLE", jeqp_table_html)

    # Update timestamp
    now_date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    content = replace_marker(content, "LAST_UPDATED", f"Updated: {now_date}")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Successfully updated market/index.html!")


if __name__ == "__main__":
    main()
