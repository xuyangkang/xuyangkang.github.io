#!/usr/bin/env python3
"""
scripts/generate_exercise_svgs.py
Generates clean, unified, lightweight SVG motion diagrams for Convict Conditioning
exercises to ensure 100% visual coverage across all 60 steps.
"""

import os

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "gym", "assets"))
os.makedirs(ASSETS_DIR, exist_ok=True)


def build_svg(title: str, step_label: str, target: str, cue: str, apparatus_svg: str, figure_svg: str, arrow_svg: str = "") -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#f1f5f9"/>
    </linearGradient>
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#2563eb"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#10b981"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="400" height="240" rx="12" fill="url(#bgGrad)" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Top Info Badge -->
  <g transform="translate(16, 20)">
    <rect width="70" height="22" rx="4" fill="#eff6ff" stroke="rgba(37,99,235,0.2)" stroke-width="1"/>
    <text x="35" y="15" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="700" fill="#2563eb">{step_label}</text>
    
    <text x="78" y="16" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="800" fill="#0f172a">{title}</text>
    <text x="368" y="16" text-anchor="end" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">🎯 {target}</text>
  </g>

  <!-- Floor / Ground Line -->
  <line x1="30" y1="185" x2="370" y2="185" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4 4"/>

  <!-- Apparatus / Scene -->
  {apparatus_svg}

  <!-- Figure Graphics (Start Pose & Finish Pose) -->
  {figure_svg}

  <!-- Trajectory / Motion Arrow -->
  {arrow_svg}

  <!-- Bottom Technique Cue -->
  <g transform="translate(200, 218)">
    <rect x="-140" y="-14" width="280" height="22" rx="11" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="drop-shadow(0 1px 2px rgba(0,0,0,0.04))"/>
    <text x="0" y="1" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#334155">💡 要领：{cue}</text>
  </g>
</svg>"""


# Definitions of SVGs to generate
SVGS = {
    # ================= 俯卧撑 =================
    "pushups-step1.svg": {
        "title": "墙壁俯卧撑", "step": "第 1 式", "target": "肩关节 / 腕部 / 胸肌", "cue": "面对墙壁双臂推墙 · 慢下慢起 · 核心绷紧",
        "apparatus": '<line x1="320" y1="50" x2="320" y2="185" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>',
        "figure": '''
          <!-- Start Pose (Tilted) -->
          <g opacity="0.35" stroke="#64748b" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <line x1="160" y1="185" x2="270" y2="105"/>
            <circle cx="280" cy="95" r="10" fill="#64748b"/>
            <line x1="250" y1="115" x2="320" y2="115"/>
          </g>
          <!-- Active Finish Pose (Bent Arms to Wall) -->
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <line x1="160" y1="185" x2="295" y2="105"/>
            <circle cx="305" cy="95" r="10" fill="#2563eb"/>
            <!-- Arms bent -->
            <polyline points="280,115 300,135 320,115"/>
          </g>
        ''',
        "arrow": '<path d="M 270 95 Q 285 90 295 95" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pushups-step2.svg": {
        "title": "上斜俯卧撑", "step": "第 2 式", "target": "胸大肌 / 三头肌", "cue": "双手撑桌椅边缘 (45°) · 躯干笔直如钢板",
        "apparatus": '''
          <rect x="250" y="130" width="70" height="10" rx="3" fill="#64748b"/>
          <line x1="260" y1="140" x2="260" y2="185" stroke="#64748b" stroke-width="4"/>
          <line x1="310" y1="140" x2="310" y2="185" stroke="#64748b" stroke-width="4"/>
        ''',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <line x1="120" y1="185" x2="245" y2="120"/>
            <circle cx="258" cy="112" r="10" fill="#2563eb"/>
            <polyline points="230,126 242,145 255,130"/>
          </g>
        ''',
        "arrow": '<path d="M 235 110 Q 248 118 255 124" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pushups-step3.svg": {
        "title": "跪姿俯卧撑", "step": "第 3 式", "target": "胸大肌 / 上肢推力", "cue": "双膝着地 · 头至膝盖直线 · 胸口轻触地面",
        "apparatus": '<rect x="110" y="180" width="40" height="5" rx="2" fill="#94a3b8"/>',
        "figure": '''
          <g opacity="0.35" stroke="#64748b" stroke-width="5" stroke-linecap="round" fill="none">
            <line x1="120" y1="185" x2="260" y2="135"/>
            <circle cx="270" cy="130" r="10" fill="#64748b"/>
            <line x1="240" y1="142" x2="240" y2="185"/>
          </g>
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <line x1="120" y1="185" x2="270" y2="175"/>
            <circle cx="282" cy="170" r="10" fill="#2563eb"/>
            <polyline points="250,175 260,160 250,185"/>
          </g>
        ''',
        "arrow": '<path d="M 255 138 L 265 162" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pushups-step4.svg": {
        "title": "半程俯卧撑", "step": "第 4 式", "target": "胸肌中束 / 肱三头肌", "cue": "标准撑地姿势 · 胸下垫篮球下沉一半深度",
        "apparatus": '<circle cx="240" cy="172" r="12" fill="#f97316"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <line x1="100" y1="185" x2="275" y2="155"/>
            <circle cx="288" cy="150" r="10" fill="#2563eb"/>
            <polyline points="250,158 262,170 250,185"/>
          </g>
        ''',
        "arrow": '<path d="M 250 145 L 250 160" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pushups-step7.svg": {
        "title": "偏重俯卧撑", "step": "第 7 式", "target": "单侧胸肌 / 核心抗旋转", "cue": "主手撑地 · 副手垫在篮球上 · 主力侧完全承重",
        "apparatus": '<circle cx="270" cy="170" r="14" fill="#f97316"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <line x1="100" y1="185" x2="270" y2="165"/>
            <circle cx="283" cy="160" r="10" fill="#2563eb"/>
            <!-- Main arm on floor -->
            <polyline points="245,168 235,150 225,185"/>
            <!-- Secondary arm on ball -->
            <line x1="255" y1="166" x2="270" y2="156"/>
          </g>
        ''',
        "arrow": '<path d="M 235 140 L 235 155" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pushups-step8.svg": {
        "title": "半程单手俯卧撑", "step": "第 8 式", "target": "单侧极致推力", "cue": "双脚分开 · 单手置于胸下 · 胸下垫球控制半程",
        "apparatus": '<circle cx="235" cy="172" r="12" fill="#f97316"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <line x1="100" y1="185" x2="260" y2="155"/>
            <circle cx="272" cy="150" r="10" fill="#2563eb"/>
            <!-- Single supporting arm -->
            <polyline points="230,158 245,170 230,185"/>
            <!-- Arm behind back -->
            <path d="M 215 160 Q 200 155 190 165"/>
          </g>
        ''',
        "arrow": '<path d="M 235 145 L 235 160" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pushups-step9.svg": {
        "title": "杠杆俯卧撑", "step": "第 9 式", "target": "单臂主推 / 三角肌", "cue": "单臂主推 · 辅助手侧向伸直按球滑动维持平衡",
        "apparatus": '<circle cx="310" cy="170" r="14" fill="#f97316"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <line x1="100" y1="185" x2="250" y2="170"/>
            <circle cx="262" cy="165" r="10" fill="#2563eb"/>
            <!-- Main push arm -->
            <polyline points="225,172 235,155 220,185"/>
            <!-- Outstretched straight arm to ball -->
            <line x1="240" y1="171" x2="310" y2="156"/>
          </g>
        ''',
        "arrow": '<path d="M 225 145 L 225 165" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pushups-step10.svg": {
        "title": "终极单手俯卧撑", "step": "第 10 式", "target": "全身刚性 / 单臂封神", "cue": "纯单臂支撑 · 双脚微宽 · 躯干水平下潜推起",
        "apparatus": '',
        "figure": '''
          <g stroke="#10b981" stroke-width="6" stroke-linecap="round" fill="none">
            <line x1="90" y1="185" x2="250" y2="168"/>
            <circle cx="263" cy="162" r="11" fill="#10b981"/>
            <!-- Single bent power arm -->
            <polyline points="220,170 235,150 215,185"/>
            <!-- Arm resting on back -->
            <path d="M 195 170 Q 180 162 175 175"/>
          </g>
        ''',
        "arrow": '<path d="M 220 140 L 220 165" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>'
    },

    # ================= 深蹲 =================
    "squats-step1.svg": {
        "title": "肩倒立深蹲", "step": "第 1 式", "target": "膝关节 / 腘绳肌", "cue": "肩倒立仰卧支撑 · 双腿悬空屈膝伸展 · 零关节压力",
        "apparatus": '',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Torso inverted on shoulders -->
            <circle cx="160" cy="180" r="10" fill="#2563eb"/>
            <line x1="170" y1="180" x2="210" y2="135"/>
            <!-- Hands supporting lower back -->
            <polyline points="180,185 195,160 210,140"/>
            <!-- Squatting legs in air -->
            <polyline points="210,135 240,110 220,70"/>
          </g>
        ''',
        "arrow": '<path d="M 240 70 Q 255 90 240 110" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "squats-step2.svg": {
        "title": "折刀深蹲", "step": "第 2 式", "target": "股四头肌 / 髋屈肌", "cue": "双手扶桌椅分担体重 · 顺畅全幅度下蹲到底",
        "apparatus": '<rect x="250" y="115" width="60" height="10" rx="3" fill="#64748b"/><line x1="280" y1="125" x2="280" y2="185" stroke="#64748b" stroke-width="4"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Squatting legs -->
            <polyline points="170,185 200,165 170,150"/>
            <line x1="170" y1="150" x2="230" y2="115"/>
            <circle cx="240" cy="105" r="10" fill="#2563eb"/>
            <!-- Hands supporting on desk -->
            <line x1="220" y1="120" x2="255" y2="115"/>
          </g>
        ''',
        "arrow": '<path d="M 180 135 L 180 155" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "squats-step3.svg": {
        "title": "支撑深蹲", "step": "第 3 式", "target": "股四头肌 / 韧带柔韧性", "cue": "双手抓扶门框或柱子 · 深蹲至大腿贴小腿 · 仅力竭借力",
        "apparatus": '<line x1="260" y1="60" x2="260" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <polyline points="180,185 220,170 190,155"/>
            <line x1="190" y1="155" x2="230" y2="115"/>
            <circle cx="235" cy="100" r="10" fill="#2563eb"/>
            <line x1="220" y1="125" x2="260" y2="125"/>
          </g>
        ''',
        "arrow": '<path d="M 190 130 L 190 155" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "squats-step4.svg": {
        "title": "半程深蹲", "step": "第 4 式", "target": "大腿肌群 / 核心平衡", "cue": "无任何借力站立 · 下蹲至大腿与地面呈 45° 慢起",
        "apparatus": '',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <polyline points="180,185 210,140 180,110"/>
            <line x1="180" y1="110" x2="195" y2="70"/>
            <circle cx="200" cy="58" r="10" fill="#2563eb"/>
            <!-- Arms forward for balance -->
            <line x1="190" y1="80" x2="230" y2="80"/>
          </g>
        ''',
        "arrow": '<path d="M 195 90 L 195 110" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "squats-step6.svg": {
        "title": "窄距深蹲", "step": "第 6 式", "target": "脚踝柔韧性 / 股四头外侧", "cue": "双脚并拢脚跟相贴 · 保持平衡全蹲到底 · 严禁内扣",
        "apparatus": '',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <polyline points="190,185 230,175 200,160"/>
            <line x1="200" y1="160" x2="215" y2="110"/>
            <circle cx="220" cy="98" r="10" fill="#2563eb"/>
            <line x1="210" y1="120" x2="250" y2="120"/>
          </g>
        ''',
        "arrow": '<path d="M 210 130 L 210 160" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "squats-step7.svg": {
        "title": "偏重深蹲", "step": "第 7 式", "target": "单腿力量分化", "cue": "一脚踩平 · 前脚踏篮球 · 重心完全压在主力腿",
        "apparatus": '<circle cx="260" cy="172" r="13" fill="#f97316"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Main leg squat -->
            <polyline points="170,185 210,170 180,155"/>
            <!-- Front leg on ball -->
            <polyline points="180,155 225,160 260,160"/>
            <line x1="180" y1="155" x2="195" y2="105"/>
            <circle cx="200" cy="92" r="10" fill="#2563eb"/>
          </g>
        ''',
        "arrow": '<path d="M 180 125 L 180 155" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "squats-step8.svg": {
        "title": "半程单腿深蹲", "step": "第 8 式", "target": "单腿离心控制 / 臀大肌", "cue": "前腿悬空伸直 · 主力腿下蹲至椅子高度 (90°) 慢起",
        "apparatus": '<line x1="220" y1="150" x2="260" y2="150" stroke="#94a3b8" stroke-dasharray="3 3"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Main leg squatting halfway -->
            <polyline points="180,185 210,145 180,130"/>
            <!-- Other leg extended forward -->
            <polyline points="180,130 220,135 260,135"/>
            <line x1="180" y1="130" x2="195" y2="80"/>
            <circle cx="200" cy="68" r="10" fill="#2563eb"/>
            <line x1="190" y1="90" x2="230" y2="90"/>
          </g>
        ''',
        "arrow": '<path d="M 180 110 L 180 130" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "squats-step9.svg": {
        "title": "辅助单腿深蹲", "step": "第 9 式", "target": "全幅度单腿深蹲过渡", "cue": "手扶篮球或桌腿微量平衡 · 前腿伸直 · 全幅单腿蹲起",
        "apparatus": '<circle cx="270" cy="172" r="13" fill="#f97316"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Squatting leg down -->
            <polyline points="160,185 200,180 170,165"/>
            <!-- Extended front leg -->
            <line x1="170" y1="165" x2="250" y2="165"/>
            <line x1="170" y1="165" x2="185" y2="115"/>
            <circle cx="190" cy="102" r="10" fill="#2563eb"/>
            <!-- Hand touching ball for balance -->
            <line x1="185" y1="125" x2="270" y2="160"/>
          </g>
        ''',
        "arrow": '<path d="M 170 135 L 170 165" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },

    # ================= 引体向上 =================
    "pullups-step1.svg": {
        "title": "垂直引体", "step": "第 1 式", "target": "背阔肌激活 / 零负荷拉力", "cue": "手抓门框垂直立柱 · 双脚贴地 · 靠上背将胸口拉近",
        "apparatus": '<line x1="280" y1="50" x2="280" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <!-- Standing tilted -->
            <line x1="180" y1="185" x2="230" y2="105"/>
            <circle cx="236" cy="92" r="10" fill="#2563eb"/>
            <!-- Pulling arms to post -->
            <polyline points="220,115 250,115 280,115"/>
          </g>
        ''',
        "arrow": '<path d="M 220 95 L 250 95" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pullups-step4.svg": {
        "title": "半程引体向上", "step": "第 4 式", "target": "肱二头肌 / 肘屈肌耐力", "cue": "悬空无踏板 · 从肘屈 90° 开始拉到下巴过杠",
        "apparatus": '<line x1="120" y1="55" x2="280" y2="55" stroke="#475569" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <!-- Body suspended -->
            <line x1="200" y1="170" x2="200" y2="105"/>
            <circle cx="200" cy="92" r="10" fill="#2563eb"/>
            <!-- 90 degree arms to bar -->
            <polyline points="200,105 180,75 185,55"/>
            <polyline points="200,105 220,75 215,55"/>
          </g>
        ''',
        "arrow": '<path d="M 200 115 L 200 90" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pullups-step7.svg": {
        "title": "偏重引体向上", "step": "第 7 式", "target": "单侧背阔肌强化", "cue": "主手握横杆 · 副手抓毛巾下端 · 单侧承担 80% 体重",
        "apparatus": '''
          <line x1="120" y1="55" x2="280" y2="55" stroke="#475569" stroke-width="6"/>
          <!-- Towel hanging -->
          <line x1="220" y1="55" x2="220" y2="95" stroke="#f59e0b" stroke-width="4"/>
        ''',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <line x1="190" y1="170" x2="190" y2="105"/>
            <circle cx="190" cy="92" r="10" fill="#2563eb"/>
            <!-- Main arm on bar -->
            <line x1="190" y1="100" x2="175" y2="55"/>
            <!-- Secondary arm holding towel -->
            <line x1="190" y1="100" x2="220" y2="90"/>
          </g>
        ''',
        "arrow": '<path d="M 190 120 L 190 95" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pullups-step8.svg": {
        "title": "半程单手引体", "step": "第 8 式", "target": "单臂极限拉力", "cue": "单臂抓杠 · 副手握腕 · 肘屈 90° 启动拉过杠",
        "apparatus": '<line x1="120" y1="55" x2="280" y2="55" stroke="#475569" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <line x1="200" y1="170" x2="200" y2="105"/>
            <circle cx="200" cy="92" r="10" fill="#2563eb"/>
            <!-- Main arm bent 90 -->
            <polyline points="200,105 185,75 190,55"/>
            <!-- Hand grabbing wrist -->
            <polyline points="200,105 210,95 190,65"/>
          </g>
        ''',
        "arrow": '<path d="M 200 115 L 200 85" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pullups-step9.svg": {
        "title": "辅助单手引体", "step": "第 9 式", "target": "近乎纯单臂拉力", "cue": "单臂握单杠 · 副手仅抓毛巾最下端维系微小平衡",
        "apparatus": '''
          <line x1="120" y1="55" x2="280" y2="55" stroke="#475569" stroke-width="6"/>
          <line x1="235" y1="55" x2="235" y2="115" stroke="#f59e0b" stroke-width="3"/>
        ''',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" fill="none">
            <line x1="190" y1="175" x2="190" y2="110"/>
            <circle cx="190" cy="98" r="10" fill="#2563eb"/>
            <!-- Single full arm on bar -->
            <line x1="190" y1="105" x2="180" y2="55"/>
            <!-- Secondary hand on towel bottom -->
            <line x1="190" y1="110" x2="235" y2="115"/>
          </g>
        ''',
        "arrow": '<path d="M 185 115 L 185 85" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "pullups-step10.svg": {
        "title": "终极单手引体向上", "step": "第 10 式", "target": "自重拉力巅峰", "cue": "纯单臂死悬垂启动 · 毫无晃动拉起 · 下巴过杠",
        "apparatus": '<line x1="120" y1="55" x2="280" y2="55" stroke="#475569" stroke-width="6"/>',
        "figure": '''
          <g stroke="#10b981" stroke-width="6" stroke-linecap="round" fill="none">
            <line x1="200" y1="170" x2="200" y2="105"/>
            <circle cx="200" cy="92" r="11" fill="#10b981"/>
            <!-- Powerful single bent arm -->
            <polyline points="200,105 185,75 195,55"/>
            <!-- Other arm behind back -->
            <path d="M 200 115 Q 215 125 210 140"/>
          </g>
        ''',
        "arrow": '<path d="M 200 120 L 200 80" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>'
    },

    # ================= 举腿 =================
    "leg_raises-step3.svg": {
        "title": "平卧曲举", "step": "第 3 式", "target": "腹直肌下束 / 髋屈肌", "cue": "仰卧微屈膝锁定钝角 (135°) · 抬腿至髋部 90° 慢放",
        "apparatus": '',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Torso flat on ground -->
            <circle cx="130" cy="180" r="10" fill="#2563eb"/>
            <line x1="140" y1="185" x2="220" y2="185"/>
            <!-- Bent leg raised to 90 degrees -->
            <polyline points="220,185 240,120 280,95"/>
          </g>
        ''',
        "arrow": '<path d="M 280 160 Q 285 120 265 100" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "leg_raises-step4.svg": {
        "title": "平卧蛙举", "step": "第 4 式", "target": "腹壁耐力 / 动态收缩", "cue": "直腿抬起到高点 · 屈膝收腹顶峰收缩 · 再伸直慢放",
        "apparatus": '',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="130" cy="180" r="10" fill="#2563eb"/>
            <line x1="140" y1="185" x2="220" y2="185"/>
            <!-- Frog tuck position -->
            <polyline points="220,185 205,130 240,110"/>
          </g>
        ''',
        "arrow": '<path d="M 260 165 Q 260 120 230 115" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "leg_raises-step6.svg": {
        "title": "悬垂屈膝", "step": "第 6 式", "target": "悬垂握力 / 下腹收缩", "cue": "悬挂单杠无晃动 · 屈膝缓慢抬至胸前顶峰收缩",
        "apparatus": '<line x1="140" y1="55" x2="260" y2="55" stroke="#475569" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="200" cy="85" r="10" fill="#2563eb"/>
            <!-- Straight arms -->
            <line x1="190" y1="55" x2="195" y2="90"/>
            <line x1="210" y1="55" x2="205" y2="90"/>
            <line x1="200" y1="95" x2="200" y2="140"/>
            <!-- Knees tucked up -->
            <polyline points="200,140 230,120 215,155"/>
          </g>
        ''',
        "arrow": '<path d="M 210 170 Q 240 160 230 130" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "leg_raises-step7.svg": {
        "title": "悬垂曲举", "step": "第 7 式", "target": "腹直肌 / 髂腰肌", "cue": "悬垂膝盖锁定大钝角 · 平稳抬大腿至与躯干垂直",
        "apparatus": '<line x1="140" y1="55" x2="260" y2="55" stroke="#475569" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="200" cy="85" r="10" fill="#2563eb"/>
            <line x1="190" y1="55" x2="195" y2="90"/>
            <line x1="210" y1="55" x2="205" y2="90"/>
            <line x1="200" y1="95" x2="200" y2="140"/>
            <!-- Bent legs to 90 degrees -->
            <polyline points="200,140 240,140 270,165"/>
          </g>
        ''',
        "arrow": '<path d="M 210 175 Q 260 175 250 145" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "leg_raises-step8.svg": {
        "title": "悬垂蛙举", "step": "第 8 式", "target": "核心控制力 / 腹壁深层", "cue": "悬垂直腿抬高 · 在顶点屈膝挤压 · 再伸直慢放",
        "apparatus": '<line x1="140" y1="55" x2="260" y2="55" stroke="#475569" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="200" cy="85" r="10" fill="#2563eb"/>
            <line x1="190" y1="55" x2="195" y2="90"/>
            <line x1="210" y1="55" x2="205" y2="90"/>
            <line x1="200" y1="95" x2="200" y2="140"/>
            <!-- Frog tuck at apex -->
            <polyline points="200,140 235,115 210,120"/>
          </g>
        ''',
        "arrow": '<path d="M 220 170 Q 255 150 235 115" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "leg_raises-step9.svg": {
        "title": "悬垂半程直举", "step": "第 9 式", "target": "L-Sit 静态杠杆力量", "cue": "双腿完全锁死笔直 · 慢速抬至水平 90° (L型) 慢放",
        "apparatus": '<line x1="140" y1="55" x2="260" y2="55" stroke="#475569" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="200" cy="85" r="10" fill="#2563eb"/>
            <line x1="190" y1="55" x2="195" y2="90"/>
            <line x1="210" y1="55" x2="205" y2="90"/>
            <line x1="200" y1="95" x2="200" y2="140"/>
            <!-- Straight leg horizontal L-sit -->
            <line x1="200" y1="140" x2="275" y2="140"/>
          </g>
        ''',
        "arrow": '<path d="M 215 175 Q 275 175 270 145" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "leg_raises-step10.svg": {
        "title": "终极悬垂直举", "step": "第 10 式", "target": "下腹 / 核心折叠神技", "cue": "双腿笔直并拢毫无摆荡 · 画弧上扬直到脚触单杠",
        "apparatus": '<line x1="140" y1="55" x2="260" y2="55" stroke="#475569" stroke-width="6"/>',
        "figure": '''
          <g stroke="#10b981" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="200" cy="85" r="11" fill="#10b981"/>
            <line x1="190" y1="55" x2="195" y2="90"/>
            <line x1="210" y1="55" x2="205" y2="90"/>
            <line x1="200" y1="95" x2="200" y2="135"/>
            <!-- Straight legs touching bar -->
            <line x1="200" y1="135" x2="245" y2="60"/>
          </g>
        ''',
        "arrow": '<path d="M 210 175 Q 290 140 250 65" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>'
    },

    # ================= 桥 =================
    "bridges-step2.svg": {
        "title": "直桥", "step": "第 2 式", "target": "脊柱伸肌 / 后链平直", "cue": "双手置于身后坐地 · 推起骨盆躯干与腿成一直线",
        "apparatus": '',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="140" cy="120" r="10" fill="#2563eb"/>
            <!-- Straight plank bridge -->
            <line x1="140" y1="130" x2="280" y2="185"/>
            <!-- Hands supporting on floor behind hips -->
            <line x1="160" y1="140" x2="160" y2="185"/>
          </g>
        ''',
        "arrow": '<path d="M 210 175 L 210 150" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "bridges-step3.svg": {
        "title": "角度桥", "step": "第 3 式", "target": "脊柱后弯感知", "cue": "双脚垫在桌椅上 · 双手撑头侧 · 体验后屈反弓",
        "apparatus": '<rect x="250" y="145" width="60" height="10" rx="3" fill="#64748b"/><line x1="280" y1="155" x2="280" y2="185" stroke="#64748b" stroke-width="4"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="130" cy="180" r="10" fill="#2563eb"/>
            <!-- Bridge arch -->
            <path d="M 140 185 Q 180 120 260 145"/>
            <polyline points="145,185 135,160 145,150"/>
          </g>
        ''',
        "arrow": '<path d="M 180 160 L 180 135" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "bridges-step4.svg": {
        "title": "头桥", "step": "第 4 式", "target": "颈椎稳定 / 背部深层小肌", "cue": "头顶垫软毛巾轻触地面 · 双手协助承重 · 严禁暴冲",
        "apparatus": '<rect x="130" y="180" width="20" height="5" rx="2" fill="#94a3b8"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Head on floor -->
            <circle cx="140" cy="178" r="9" fill="#2563eb"/>
            <!-- Arch to feet -->
            <path d="M 140 178 Q 190 120 250 185"/>
            <!-- Hands beside head -->
            <line x1="145" y1="165" x2="155" y2="185"/>
          </g>
        ''',
        "arrow": '<path d="M 190 160 L 190 135" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "bridges-step5.svg": {
        "title": "半桥", "step": "第 5 式", "target": "胸椎伸展 / 骨盆前侧拉伸", "cue": "背部垫篮球或泡沫轴 · 双手推起脊柱悬空离开球体",
        "apparatus": '<circle cx="190" cy="172" r="13" fill="#f97316"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <circle cx="130" cy="165" r="10" fill="#2563eb"/>
            <!-- Higher arch clearance over ball -->
            <path d="M 130 175 Q 190 120 250 185"/>
            <polyline points="135,175 125,160 135,185"/>
          </g>
        ''',
        "arrow": '<path d="M 190 155 L 190 130" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "bridges-step7.svg": {
        "title": "下行壁行桥", "step": "第 7 式", "target": "站立后弯控制", "cue": "背对墙壁站立 · 双手摸墙一步步向下“走”到地面",
        "apparatus": '<line x1="280" y1="50" x2="280" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <line x1="180" y1="185" x2="190" y2="135"/>
            <!-- Backward arch to wall -->
            <path d="M 190 135 Q 230 110 275 130"/>
            <circle cx="240" cy="110" r="10" fill="#2563eb"/>
          </g>
        ''',
        "arrow": '<path d="M 275 90 L 275 130" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "bridges-step8.svg": {
        "title": "上行壁行桥", "step": "第 8 式", "target": "后链回弹力量", "cue": "从地面全桥姿势起步 · 手摸墙一步步往上“走”回站立",
        "apparatus": '<line x1="280" y1="50" x2="280" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <line x1="180" y1="185" x2="190" y2="135"/>
            <path d="M 190 135 Q 230 100 275 90"/>
            <circle cx="240" cy="98" r="10" fill="#2563eb"/>
          </g>
        ''',
        "arrow": '<path d="M 275 130 L 275 90" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "bridges-step9.svg": {
        "title": "合桥", "step": "第 9 式", "target": "自由下潜柔韧性", "cue": "站立向后完全下弯起桥 · 双手轻柔触地吸震",
        "apparatus": '',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Full arched back from standing to ground touch -->
            <path d="M 230 185 Q 180 85 130 185"/>
            <circle cx="160" cy="120" r="10" fill="#2563eb"/>
            <!-- Arms almost at floor -->
            <polyline points="140,140 125,165 130,185"/>
          </g>
        ''',
        "arrow": '<path d="M 150 110 Q 125 135 125 165" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "bridges-step10.svg": {
        "title": "终极铁板桥", "step": "第 10 式", "target": "脊柱如钢缆弹簧", "cue": "站立顺畅后弯成桥 · 略作停顿凭借核心弹力直接站起！",
        "apparatus": '',
        "figure": '''
          <g stroke="#10b981" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <path d="M 240 185 Q 185 85 130 185"/>
            <circle cx="165" cy="115" r="11" fill="#10b981"/>
          </g>
        ''',
        "arrow": '<path d="M 135 165 Q 140 115 170 95" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>'
    },

    # ================= 倒立撑 =================
    "handstands-step2.svg": {
        "title": "乌鸦式", "step": "第 2 式", "target": "手腕韧带 / 核心平衡", "cue": "双手撑地 · 双膝顶手肘窝外侧 · 双脚离地平衡静态保持",
        "apparatus": '',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Hands on floor -->
            <polyline points="200,185 200,145 220,135"/>
            <!-- Torso leaned forward -->
            <line x1="220" y1="135" x2="250" y2="120"/>
            <circle cx="262" cy="115" r="10" fill="#2563eb"/>
            <!-- Legs tucked on elbow -->
            <polyline points="220,135 195,125 175,145"/>
          </g>
        ''',
        "arrow": '<path d="M 160 165 Q 170 145 185 135" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "handstands-step3.svg": {
        "title": "靠墙倒立", "step": "第 3 式", "target": "肩部静态耐力 / 全身倒立线", "cue": "手距墙 20cm 撑地 · 蹬地起倒立 · 身体笔直脚跟靠墙",
        "apparatus": '<line x1="240" y1="50" x2="240" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Hands on floor -->
            <line x1="210" y1="185" x2="210" y2="140"/>
            <!-- Inverted head -->
            <circle cx="210" cy="155" r="10" fill="#2563eb"/>
            <!-- Inverted body leaning against wall -->
            <line x1="210" y1="140" x2="235" y2="60"/>
          </g>
        ''',
        "arrow": '<path d="M 210 110 L 210 75" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "handstands-step4.svg": {
        "title": "半程倒立撑", "step": "第 4 式", "target": "肩三角肌前束 / 肘推力", "cue": "靠墙倒立 · 头下垫枕头/瑜伽砖 · 下落一半深度推起",
        "apparatus": '''
          <line x1="240" y1="50" x2="240" y2="185" stroke="#64748b" stroke-width="6"/>
          <rect x="195" y="165" width="30" height="20" rx="3" fill="#cbd5e1"/>
        ''',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <polyline points="190,185 190,150 205,140"/>
            <polyline points="220,185 220,150 205,140"/>
            <circle cx="205" cy="148" r="10" fill="#2563eb"/>
            <line x1="205" y1="140" x2="235" y2="60"/>
          </g>
        ''',
        "arrow": '<path d="M 205 130 L 205 145" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "handstands-step5.svg": {
        "title": "标准靠墙倒立撑", "step": "第 5 式", "target": "肩上推力分水岭", "cue": "慢放到底头顶轻吻地面 · 不借回弹 · 纯力推至手臂锁死",
        "apparatus": '<line x1="240" y1="50" x2="240" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Deep bent elbows -->
            <polyline points="180,185 180,165 200,160"/>
            <polyline points="220,185 220,165 200,160"/>
            <circle cx="200" cy="175" r="9" fill="#2563eb"/>
            <line x1="200" y1="160" x2="235" y2="60"/>
          </g>
        ''',
        "arrow": '<path d="M 200 150 L 200 170" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "handstands-step6.svg": {
        "title": "窄距倒立撑", "step": "第 6 式", "target": "肱三头肌外侧 / 肩内侧", "cue": "两手间距两拳以内 · 考验手腕柔韧性与三头肌爆发力",
        "apparatus": '<line x1="240" y1="50" x2="240" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <polyline points="195,185 185,160 200,150"/>
            <polyline points="215,185 225,160 200,150"/>
            <circle cx="200" cy="165" r="10" fill="#2563eb"/>
            <line x1="200" y1="150" x2="235" y2="60"/>
          </g>
        ''',
        "arrow": '<path d="M 200 140 L 200 160" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "handstands-step7.svg": {
        "title": "偏重倒立撑", "step": "第 7 式", "target": "单侧肩部承重分化", "cue": "一手垫砖高出地面 · 70% 自重集中在主力手深潜推直",
        "apparatus": '''
          <line x1="240" y1="50" x2="240" y2="185" stroke="#64748b" stroke-width="6"/>
          <rect x="215" y="172" width="20" height="13" rx="2" fill="#cbd5e1"/>
        ''',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Floor hand -->
            <polyline points="180,185 175,160 195,150"/>
            <!-- Brick hand -->
            <polyline points="225,172 230,155 195,150"/>
            <circle cx="195" cy="162" r="10" fill="#2563eb"/>
            <line x1="195" y1="150" x2="235" y2="60"/>
          </g>
        ''',
        "arrow": '<path d="M 185 140 L 185 160" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "handstands-step8.svg": {
        "title": "半程单手倒立撑", "step": "第 8 式", "target": "单肩极限力量挑战", "cue": "单臂撑地靠墙 · 副手轻扶身侧 · 慢降一半深度强力推起",
        "apparatus": '<line x1="240" y1="50" x2="240" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <!-- Single working arm bent -->
            <polyline points="190,185 180,155 200,145"/>
            <circle cx="200" cy="158" r="10" fill="#2563eb"/>
            <line x1="200" y1="145" x2="235" y2="60"/>
            <!-- Free hand at side -->
            <path d="M 200 135 Q 215 130 210 115"/>
          </g>
        ''',
        "arrow": '<path d="M 195 130 L 195 150" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "handstands-step9.svg": {
        "title": "杠杆倒立撑", "step": "第 9 式", "target": "单臂孤立肩推", "cue": "单手主力支撑 · 副手侧向轻抚墙壁维系微小平衡",
        "apparatus": '<line x1="260" y1="50" x2="260" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#2563eb" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
            <polyline points="190,185 180,160 200,150"/>
            <circle cx="200" cy="162" r="10" fill="#2563eb"/>
            <line x1="200" y1="150" x2="245" y2="60"/>
            <!-- Lever arm reaching to wall -->
            <line x1="205" y1="145" x2="260" y2="120"/>
          </g>
        ''',
        "arrow": '<path d="M 190 140 L 190 160" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)"/>'
    },
    "handstands-step10.svg": {
        "title": "终极单手倒立撑", "step": "第 10 式", "target": "肩部封神王冠", "cue": "纯单臂撑地 · 身体慢放到底再不可思议推直 · 徒手神技",
        "apparatus": '<line x1="250" y1="50" x2="250" y2="185" stroke="#64748b" stroke-width="6"/>',
        "figure": '''
          <g stroke="#10b981" stroke-width="6" stroke-linecap="round" fill="none">
            <polyline points="195,185 185,160 205,150"/>
            <circle cx="205" cy="165" r="11" fill="#10b981"/>
            <line x1="205" y1="150" x2="245" y2="60"/>
            <!-- Free arm behind back -->
            <path d="M 210 135 Q 225 125 215 110"/>
          </g>
        ''',
        "arrow": '<path d="M 195 135 L 195 160" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowGreen)"/>'
    },
}

def generate_all():
    count = 0
    for filename, data in SVGS.items():
        svg_content = build_svg(
            title=data["title"],
            step_label=data["step"],
            target=data["target"],
            cue=data["cue"],
            apparatus_svg=data.get("apparatus", ""),
            figure_svg=data.get("figure", ""),
            arrow_svg=data.get("arrow", "")
        )
        dest_path = os.path.join(ASSETS_DIR, filename)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        count += 1
    print(f"Successfully generated {count} custom vector motion diagrams in {ASSETS_DIR}!")

if __name__ == "__main__":
    generate_all()
