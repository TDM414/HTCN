# -*- coding: utf-8 -*-
"""
Script to generate the complete, production-grade preview.html for:
"Hải Trình 1911 - 1941 | Hành Trình Của Ngọn Lửa"
University Subject: Tư tưởng Hồ Chí Minh
"""

import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="vi" class="h-full bg-slate-950 text-slate-100 antialiased select-none">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Hải Trình 1911 – 1941 | Hành Trình Của Ngọn Lửa • Tư Tưởng Hồ Chí Minh</title>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        void: '#03050a',
                        abyss: '#070c18',
                        timber: '#181411',
                        brass: '#d4a348',
                        lantern: '#f59e0b',
                        horizon: '#ea580c',
                        crimson: '#dc2626',
                        gold: '#fbbf24',
                        moderncyan: '#06b6d4',
                        modernsky: '#0284c7'
                    },
                    fontFamily: {
                        cinematic: ['"Playfair Display"', 'Georgia', 'serif'],
                        body: ['"Be Vietnam Pro"', 'system-ui', 'sans-serif'],
                        typewriter: ['"Courier Prime"', '"Courier New"', 'monospace']
                    }
                }
            }
        }
    </script>

    <!-- Google Fonts: Playfair Display, Be Vietnam Pro, Courier Prime -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600&display=swap" rel="stylesheet">

    <!-- Preload Cinematic Story Plates for Instant Smooth Transitions -->
    <link rel="preload" as="image" href="prologue_1_can_vuong.jpg">
    <link rel="preload" as="image" href="prologue_2_nguyen_tat_thanh.jpg">
    <link rel="preload" as="image" href="prologue_3_saigon_1911.jpg">
    <link rel="preload" as="image" href="inn_1_talking.jpg">
    <link rel="preload" as="image" href="inn_2_hands.jpg">
    <link rel="preload" as="image" href="inn_3_handshake.jpg">
    <link rel="preload" as="image" href="dock_1_ship.jpg">
    <link rel="preload" as="image" href="dock_2_register.jpg">
    <link rel="preload" as="image" href="dock_3_gangway.jpg">
    <link rel="preload" as="image" href="ship_1_boiler.jpg">
    <link rel="preload" as="image" href="ship_2_study.jpg">
    <link rel="preload" as="image" href="act4_1_paris_lenin.jpg">
    <link rel="preload" as="image" href="act4_2_guangzhou_school.jpg">
    <link rel="preload" as="image" href="act4_3_party_founded.jpg">
    <link rel="preload" as="image" href="act5_1_pacbo_return.jpg">
    <link rel="preload" as="image" href="act5_2_pacbo_lamp.jpg">
    <link rel="preload" as="image" href="act5_3_sunrise_independence.jpg">

    <style>
        :root {
            --color-void: #03050a;
            --color-abyss: #070c18;
            --color-brass: #d4a348;
            --color-brass-glow: rgba(212, 163, 72, 0.45);
            --color-lantern: #f59e0b;
            --color-crimson: #dc2626;
            --ease-cinematic: cubic-bezier(0.16, 1, 0.3, 1);
            --ease-snap: cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        body {
            font-family: 'Be Vietnam Pro', system-ui, sans-serif;
            background-color: var(--color-void);
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }

        .font-cinematic { font-family: 'Playfair Display', serif; }
        .font-typewriter { font-family: 'Courier Prime', monospace; }

        /* Theatrical 16:9 Viewport */
        .stage-viewport {
            aspect-ratio: 16 / 9;
            max-width: 100vw;
            max-height: 100vh;
            width: 100%;
            height: 100%;
            perspective: 1200px;
            transform-style: preserve-3d;
        }

        @media (min-aspect-ratio: 16/9) {
            .stage-viewport { width: auto; height: 100vh; aspect-ratio: 16 / 9; }
        }
        @media (max-aspect-ratio: 16/9) {
            .stage-viewport { width: 100vw; height: auto; aspect-ratio: 16 / 9; }
        }

        /* 2.5D Parallax Layers */
        .parallax-layer {
            position: absolute;
            inset: 0;
            will-change: transform;
            transform-style: preserve-3d;
            transition: transform 0.12s var(--ease-cinematic);
        }

        /* Shimmer & Glows */
        @keyframes pulseLantern {
            0%, 100% { opacity: 0.88; filter: drop-shadow(0 0 25px rgba(245, 158, 11, 0.7)); }
            50% { opacity: 1; filter: drop-shadow(0 0 55px rgba(245, 158, 11, 0.95)); }
        }

        @keyframes horizonDrift {
            0%, 100% { opacity: 0.65; transform: scaleY(1); }
            50% { opacity: 0.9; transform: scaleY(1.08); }
        }

        .animate-lantern { animation: pulseLantern 3.5s ease-in-out infinite; }
        .animate-horizon { animation: horizonDrift 7s ease-in-out infinite; }

        /* Dialog & Scrim */
        .dialogue-card {
            background: rgba(7, 12, 24, 0.94);
            border: 1px solid rgba(212, 163, 72, 0.42);
            box-shadow: 
                0 4px 6px -1px rgba(0, 0, 0, 0.6),
                0 25px 50px -12px rgba(0, 0, 0, 0.95),
                0 0 40px rgba(212, 163, 72, 0.18);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }

        /* Time Lens Optical Rim */
        .lens-ring {
            box-shadow: 
                0 0 0 3px rgba(212, 163, 72, 0.9),
                0 0 0 6px rgba(10, 15, 26, 0.8),
                0 0 30px rgba(212, 163, 72, 0.6),
                inset 0 0 25px rgba(6, 182, 212, 0.4);
        }

        /* Steam Lever Track */
        .lever-track {
            background: linear-gradient(180deg, #1f1b17 0%, #0d0c0b 100%);
            box-shadow: inset 0 2px 8px rgba(0,0,0,0.9), 0 0 0 1px rgba(212,163,72,0.3);
        }

        /* Striker Strip Texture on Matchbox */
        .striker-strip {
            background: repeating-linear-gradient(
                45deg,
                #2e1b10,
                #2e1b10 2px,
                #452817 2px,
                #452817 4px
            );
            box-shadow: inset 0 0 4px rgba(0,0,0,0.8);
        }

        /* Ken Burns Dynamic Cinematic Camera Keyframes */
        @keyframes kbSlide1 {
            0% { transform: scale(1.0) translate(0, 0); }
            100% { transform: scale(1.08) translate(-1.8%, 1.2%); }
        }
        @keyframes kbSlide2 {
            0% { transform: scale(1.08) translate(1.2%, 1.0%); }
            100% { transform: scale(1.02) translate(-1%, -0.8%); }
        }
        @keyframes kbSlide3 {
            0% { transform: scale(1.02) translate(-1.2%, 0.5%); }
            100% { transform: scale(1.07) translate(1.5%, -0.8%); }
        }

        .kenburns-1 { animation: kbSlide1 20s cubic-bezier(0.25, 1, 0.5, 1) forwards !important; }
        .kenburns-2 { animation: kbSlide2 20s cubic-bezier(0.25, 1, 0.5, 1) forwards !important; }
        .kenburns-3 { animation: kbSlide3 20s cubic-bezier(0.25, 1, 0.5, 1) forwards !important; }

        /* Floating Subtitles Blur Dissolve & Lift Keyframes */
        @keyframes cinemaTextIn {
            0% {
                opacity: 0;
                transform: translateY(22px);
                filter: blur(8px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
                filter: blur(0px);
            }
        }
        .cinema-title-animate {
            animation: cinemaTextIn 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .cinema-subtext-animate {
            animation: cinemaTextIn 0.95s cubic-bezier(0.16, 1, 0.3, 1) 0.2s both;
        }

        /* Parchment vintage scrollbar */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: rgba(10, 15, 26, 0.8); }
        ::-webkit-scrollbar-thumb { background: rgba(212, 163, 72, 0.4); border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(212, 163, 72, 0.7); }
    </style>
</head>
<body class="flex items-center justify-center bg-black overflow-hidden">

    <!-- 16:9 Theatrical Stage -->
    <div id="stageContainer" class="stage-viewport relative overflow-hidden bg-void flex flex-col justify-between shadow-2xl">
        
        <!-- ========================================== -->
        <!-- CINEMATIC BACKGROUND CANVAS (CROSS-FADING) -->
        <!-- ========================================== -->
        <div id="mainBgStage" class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
            <!-- Background Image Layer A -->
            <img id="bgLayerA" src="inn_1_talking.jpg" alt="Minh họa lịch sử" 
                 class="absolute inset-0 w-full h-full object-cover object-center transition-opacity duration-1000 filter brightness-[0.92] contrast-105 kenburns-1 opacity-100">
            <!-- Background Image Layer B -->
            <img id="bgLayerB" src="inn_2_hands.jpg" alt="Minh họa lịch sử dự phòng" 
                 class="absolute inset-0 w-full h-full object-cover object-center transition-opacity duration-1000 filter brightness-[0.92] contrast-105 kenburns-2 opacity-0">
            
            <!-- Atmospheric VFX Overlays -->
            <canvas id="skyCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[1]"></canvas>
            <canvas id="smokeCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[2]"></canvas>
            <canvas id="ambientFlickerCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[3]"></canvas>
            
            <!-- Vignette & Horizon Lighting -->
            <div class="absolute inset-0 bg-radial-vignette from-transparent via-black/25 to-black/85 pointer-events-none z-[4]" style="background: radial-gradient(circle at 50% 50%, transparent 45%, rgba(3,5,10,0.85) 100%);"></div>
            <div class="absolute inset-x-0 bottom-0 h-64 bg-gradient-to-t from-black via-black/70 to-transparent pointer-events-none z-[4]"></div>
            <div class="absolute inset-x-0 top-0 h-28 bg-gradient-to-b from-black/80 to-transparent pointer-events-none z-[4]"></div>
        </div>

        <!-- ========================================== -->
        <!-- HUD HEADER (METADATA & INTERACTIVE CUES) -->
        <!-- ========================================== -->
        <header class="relative z-20 flex items-center justify-between px-6 py-4 bg-gradient-to-b from-void/95 via-void/60 to-transparent pointer-events-auto">
            <div class="flex items-center gap-4">
                <button onclick="toggleChapterMenu(true)" title="Danh Sách Hồi Ký Lịch Sử (Phím C)" aria-label="Menu Hồi Ký"
                        class="w-11 h-11 rounded-full border border-brass/50 bg-abyss/90 flex items-center justify-center text-brass hover:bg-brass/20 transition-all cursor-pointer shadow-[0_0_15px_rgba(212,163,72,0.25)] focus-visible:ring-2 focus-visible:ring-brass">
                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="3" y1="12" x2="21" y2="12"></line>
                        <line x1="3" y1="6" x2="21" y2="6"></line>
                        <line x1="3" y1="18" x2="21" y2="18"></line>
                    </svg>
                </button>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-ping" aria-hidden="true"></span>
                        <span id="hudActBadge" class="text-xs font-semibold tracking-widest uppercase text-brass font-cinematic">HỒI 1 • LỜI THỀ GÁC TRỌ</span>
                    </div>
                    <h1 id="hudLocationTitle" class="text-sm md:text-base font-bold text-slate-100 tracking-wide">Căn Gác Trọ Nhỏ — Sài Gòn</h1>
                    <p id="hudCoordinates" class="text-[11px] text-slate-400 font-typewriter tracking-tight">10°46'N 106°42'E • Đầu Tháng 06/1911 (Đêm)</p>
                </div>
            </div>

            <!-- Ideological Resonance Meter -->
            <div class="hidden md:flex items-center gap-3 px-4 py-2 rounded-full border border-brass/35 bg-abyss/80 backdrop-blur-md shadow-lg">
                <svg class="w-4 h-4 text-amber-400" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                </svg>
                <div class="text-left">
                    <div class="flex justify-between items-center gap-4 text-[10px] uppercase font-semibold text-slate-300">
                        <span>Đồng Điệu Lý Tưởng</span>
                        <span id="resonanceScore" class="text-brass font-typewriter font-bold">25%</span>
                    </div>
                    <div class="w-32 h-1.5 bg-slate-800 rounded-full overflow-hidden mt-0.5">
                        <div id="resonanceBar" class="h-full bg-gradient-to-r from-amber-500 via-orange-500 to-crimson transition-all duration-700 w-1/4"></div>
                    </div>
                </div>
            </div>

            <!-- Action Buttons -->
            <div class="flex items-center gap-2">
                <!-- Thấu Kính Button -->
                <button id="btnTimeLens" onclick="toggleTimeLens()" 
                        title="Bật/Tắt Thấu Kính Xuyên Thời Gian 1911 vs 2026 (Phím T)" 
                        aria-label="Thấu kính thời gian"
                        class="min-w-[44px] min-h-[44px] px-3 py-2 rounded-xl border border-cyan-400/50 bg-cyan-950/40 hover:bg-cyan-900/60 text-cyan-300 font-cinematic text-xs font-bold tracking-wider flex items-center gap-2 cursor-pointer transition-all shadow-[0_0_15px_rgba(6,182,212,0.3)] focus-visible:ring-2 focus-visible:ring-cyan-400">
                    <svg class="w-4 h-4 text-cyan-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="8"/>
                        <line x1="12" y1="2" x2="12" y2="4"/><line x1="12" y1="20" x2="12" y2="22"/>
                        <line x1="2" y1="12" x2="4" y2="12"/><line x1="20" y1="12" x2="22" y2="12"/>
                    </svg>
                    <span class="hidden sm:inline">Thấu Kính [T]</span>
                </button>

                <!-- Chapter Menu Button -->
                <button onclick="toggleChapterMenu(true)" title="Danh Sách 5 Hồi Ký (Phím C)" aria-label="Các Hồi Lịch Sử"
                        class="min-w-[44px] min-h-[44px] px-3 py-2 rounded-xl border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass text-xs font-cinematic font-bold tracking-wider flex items-center gap-1.5 cursor-pointer transition-all">
                    <svg class="w-4 h-4 text-brass" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                    <span class="hidden md:inline">Hồi Ký [C]</span>
                </button>

                <!-- Audio Toggle -->
                <button id="btnAudioToggle" onclick="toggleAudio()" title="Bật/Tắt âm thanh (Phím M)" aria-label="Bật/Tắt âm thanh"
                        class="min-w-[44px] min-h-[44px] p-2.5 rounded-lg border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass transition-all flex items-center justify-center cursor-pointer focus-visible:ring-2 focus-visible:ring-brass">
                    <svg id="iconAudioOn" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
                        <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>
                    </svg>
                    <svg id="iconAudioOff" class="w-5 h-5 hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
                        <line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/>
                    </svg>
                </button>

                <!-- Autoplay Toggle -->
                <button id="btnAutoPlay" onclick="toggleAutoPlay()" title="Tự động dẫn truyện (Phím A)" aria-label="Tự động dẫn truyện"
                        class="min-w-[44px] min-h-[44px] p-2.5 rounded-lg border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass transition-all flex items-center justify-center cursor-pointer">
                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/>
                        <polygon points="10 8 16 12 10 16 10 8"/>
                    </svg>
                </button>

                <!-- History Log Button -->
                <button onclick="toggleLogModal(true)" title="Nhật ký hội thoại (Phím L)" aria-label="Nhật ký"
                        class="min-w-[44px] min-h-[44px] p-2.5 rounded-lg border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass transition-all flex items-center justify-center cursor-pointer">
                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <line x1="16" y1="13" x2="8" y2="13"/>
                        <line x1="16" y1="17" x2="8" y2="17"/>
                        <polyline points="10 9 9 9 8 9"/>
                    </svg>
                </button>
            </div>
        </header>

        <!-- ========================================== -->
        <!-- INTERACTIVE WORKSPACES (IN-STAGE WIDGETS) -->
        <!-- ========================================== -->

        <!-- WHISTLE LEVER (HỒI 2 CẢNG SÀI GÒN) -->
        <div id="whistleLeverStation" class="hidden absolute top-[20%] right-6 z-20 pointer-events-auto flex flex-col items-center">
            <div class="p-3 rounded-2xl bg-void/90 border border-brass/40 backdrop-blur-md shadow-2xl flex flex-col items-center group">
                <span class="text-[10px] font-cinematic uppercase tracking-widest text-brass font-bold mb-2">Cần Còi Tàu</span>
                <div id="leverTrack" class="relative w-8 h-36 lever-track rounded-full p-1 cursor-ns-resize flex justify-center">
                    <div class="w-0.5 h-full bg-brass/30 dashed"></div>
                    <div id="leverHandle" 
                         class="absolute top-2 w-7 h-9 rounded-lg bg-gradient-to-b from-amber-300 via-amber-500 to-amber-700 border border-amber-200/60 shadow-[0_4px_12px_rgba(245,158,11,0.6)] flex flex-col items-center justify-center cursor-grab active:cursor-grabbing transition-transform"
                         style="transform: translateY(0px);">
                        <div class="w-4 h-1 bg-amber-900/60 rounded-full mb-1"></div>
                        <div class="w-4 h-1 bg-amber-900/60 rounded-full"></div>
                    </div>
                </div>
                <span class="text-[9px] text-amber-300 font-typewriter mt-2 text-center leading-tight">
                    Kéo cần gạt<br>để hú 3 hồi còi
                </span>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- THEATRICAL DIALOGUE & INTERACTIVE FOOTER -->
        <!-- ========================================== -->
        <main class="relative z-20 p-4 md:p-6 flex flex-col justify-end w-full max-w-5xl mx-auto pointer-events-none">
            <div class="w-full flex flex-col gap-3 pointer-events-auto">
                
                <!-- Branching Choices Container -->
                <div id="choicesContainer" class="hidden flex flex-col gap-2 mb-1 animate-fade-in">
                    <span class="text-[11px] font-typewriter text-amber-300/90 tracking-wider uppercase flex items-center gap-1.5 px-1">
                        <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                        Lựa chọn đồng hành của bạn:
                    </span>
                    <div id="choicesList" class="grid grid-cols-1 md:grid-cols-2 gap-2.5"></div>
                </div>

                <!-- Tương Tác 2: Kéo Bàn Tay Đồng Hành (Handshake Drag) -->
                <div id="pledgeDragContainer" class="hidden flex flex-col items-center justify-center p-4 rounded-xl bg-void/95 border-2 border-amber-500/60 shadow-2xl backdrop-blur-md mb-2">
                    <div class="flex items-center gap-2 mb-2 text-center">
                        <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
                        <h4 class="font-cinematic text-sm md:text-base font-bold text-amber-200 tracking-wider uppercase">
                            Ước Hẹn 1911: Hai Bàn Tay Kết Giao Chí Hướng
                        </h4>
                    </div>
                    <p class="text-xs text-slate-300 font-light text-center mb-3">
                        Kéo bàn tay của bạn lên để nắm chặt bàn tay chai sần của Bác trước ngọn đèn dầu!
                    </p>
                    
                    <div id="handZone" class="relative w-full max-w-md h-40 bg-slate-950/80 rounded-xl border border-brass/30 flex flex-col justify-between items-center p-3 overflow-hidden select-none">
                        <!-- Van Ba's Open Hands Target -->
                        <div id="vanBaHandsTarget" class="flex flex-col items-center">
                            <div class="relative w-20 h-14 flex items-center justify-center">
                                <div class="absolute inset-0 bg-amber-500/20 rounded-full blur-md animate-pulse"></div>
                                <svg class="w-14 h-14 text-amber-400 filter drop-shadow-[0_0_10px_rgba(245,158,11,0.8)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                    <path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0"/>
                                    <path d="M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v2"/>
                                    <path d="M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"/>
                                    <path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/>
                                </svg>
                            </div>
                            <span class="text-[9px] text-amber-300 font-typewriter tracking-wider uppercase">Bàn tay Văn Ba</span>
                        </div>

                        <!-- Distance guide line -->
                        <div class="w-0.5 h-10 border-l border-dashed border-amber-400/40"></div>

                        <!-- Companion Hand Draggable -->
                        <div id="companionHandDraggable" 
                             class="flex flex-col items-center cursor-grab active:cursor-grabbing transform transition-transform"
                             style="touch-action: none;">
                            <div class="w-12 h-12 rounded-full bg-slate-800 border-2 border-amber-400 flex items-center justify-center text-amber-300 shadow-[0_0_15px_rgba(245,158,11,0.5)]">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M7 11V6a2 2 0 0 1 2-2v0a2 2 0 0 1 2 2v0"/>
                                    <path d="M11 10V4a2 2 0 0 1 2-2v0a2 2 0 0 1 2 2v2"/>
                                    <path d="M15 10.5V6a2 2 0 0 1 2-2v0a2 2 0 0 1 2 2v8"/>
                                    <path d="M7 8a2 2 0 0 0-4 0v6a8 8 0 0 0 8 8h2c2.8 0 4.5-.86 5.99-2.34l3.6-3.6a2 2 0 0 0-2.83-2.82L18 15"/>
                                </svg>
                            </div>
                            <span class="text-[9px] text-slate-300 font-typewriter tracking-wider uppercase mt-1 flex items-center gap-1">
                                <svg class="w-3 h-3 text-amber-400 animate-bounce" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg>
                                Kéo lên để siết chặt tay
                            </span>
                        </div>
                    </div>
                </div>

                <!-- Theatrical Dialogue Card -->
                <div id="dialogueBox" onclick="handleDialogueBoxClick()"
                     class="dialogue-card rounded-xl p-5 md:p-6 cursor-pointer transition-all duration-200 hover:border-brass/70 focus-visible:ring-2 focus-visible:ring-brass relative group">
                    
                    <div class="flex items-center justify-between pb-3 mb-3 border-b border-brass/25">
                        <div class="flex items-center gap-3">
                            <span id="speakerBadge" class="px-3 py-1 rounded bg-brass/20 border border-brass/40 text-brass font-cinematic text-xs md:text-sm font-bold tracking-widest uppercase">
                                Người Dẫn Truyện
                            </span>
                            <span id="speakerRole" class="text-xs text-slate-400 font-typewriter">
                                Bến Nhà Rồng • Chiều 05/06/1911
                            </span>
                        </div>
                        <div class="flex items-center gap-2 text-[11px] text-slate-400 font-typewriter">
                            <span class="hidden sm:inline">Phím [Space] / Nhấp để tiếp tục</span>
                            <svg class="w-4 h-4 text-brass animate-bounce" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
                        </div>
                    </div>

                    <div class="min-h-[72px] md:min-h-[84px] flex items-start">
                        <p id="dialogueContent" class="text-sm md:text-base leading-relaxed text-slate-100 font-normal tracking-wide"></p>
                    </div>

                    <div class="mt-3 pt-2 flex items-center justify-between text-[11px] text-slate-400 border-t border-slate-800/80">
                        <div class="flex items-center gap-1.5 font-typewriter">
                            <span id="stepActSummary">Hồi 1/5:</span>
                            <span id="stepSceneTitle" class="text-slate-200 font-semibold">Lời Thề Gác Trọ</span>
                        </div>
                        <div id="stepIndicator" class="font-typewriter text-brass font-bold">1 / 18</div>
                    </div>
                </div>

            </div>
        </main>

        <!-- ======================================================== -->
        <!-- HỒI 0: ĐÊM DÀI THUỘC ĐỊA & LỐI RẼ PHƯƠNG TÂY (PROLOGUE) -->
        <!-- ======================================================== -->
        <audio id="prologueBgmAudio" preload="auto" loop class="hidden">
            <source src="prologue_theme.mp3" type="audio/mpeg">
            <source src="prologue_theme.ogg" type="audio/ogg">
        </audio>

        <div id="prologueStage" onclick="handlePrologueBackgroundClick(event)" class="absolute inset-0 z-[60] bg-black flex flex-col justify-between p-4 md:p-8 transition-opacity duration-1000 overflow-hidden select-none cursor-pointer">
            <!-- Ken-Burns Moving Background Image -->
            <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
                <img id="prologueBgImg" src="prologue_1_can_vuong.jpg" alt="Minh họa lịch sử Hồi 0" 
                     class="w-full h-full object-cover object-center filter brightness-[0.92] contrast-105 transition-all duration-700 transform scale-100 kenburns-1">
                <canvas id="prologueVfxCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[1]"></canvas>
                <div class="absolute inset-x-0 bottom-0 h-80 bg-gradient-to-t from-black via-black/70 to-transparent z-[2]"></div>
                <div class="absolute inset-x-0 top-0 h-28 bg-gradient-to-b from-black/80 to-transparent z-[2]"></div>
            </div>

            <!-- Top Header -->
            <div class="relative z-10 flex items-center justify-between w-full max-w-6xl mx-auto pt-2 pointer-events-auto">
                <div class="flex items-center gap-3">
                    <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-black/60 border border-amber-400/50 backdrop-blur-md text-amber-300 text-[11px] md:text-xs font-cinematic uppercase tracking-widest font-bold shadow-lg">
                        <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
                        HỒI 0 • KHỞI NGUỒN TƯ TƯỞNG
                    </span>
                    <span id="prologueStepIndicator" class="text-xs text-amber-200/80 font-typewriter drop-shadow-[0_2px_4px_rgba(0,0,0,1)]">
                        Phân cảnh 1 / 3
                    </span>
                </div>

                <div id="audioStartHint" class="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-amber-500/15 border border-amber-400/40 text-amber-300 text-[11px] font-typewriter backdrop-blur-md animate-pulse shadow-md transition-opacity duration-700">
                    <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>
                    <span>Nhấp chuột hoặc [Space] để mở nhạc nền dương cầm</span>
                </div>

                <button onclick="event.stopPropagation(); skipPrologue()" class="min-h-[44px] px-4 py-2 rounded-lg border border-white/20 bg-black/50 hover:bg-black/80 backdrop-blur-md text-slate-200 hover:text-white text-xs font-typewriter transition-all flex items-center gap-2 cursor-pointer focus-visible:ring-2 focus-visible:ring-brass" title="Bỏ qua dẫn nhập vào thẳng sân khấu">
                    <span>Bỏ qua dẫn nhập</span>
                    <span class="text-[10px] text-slate-400 hidden sm:inline">[Esc]</span>
                </button>
            </div>

            <!-- Floating Subtitles Section -->
            <div class="relative z-10 w-full max-w-5xl mx-auto pb-4 md:pb-8 pointer-events-auto">
                <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                        <span id="prologueEraBadge" class="text-xs md:text-sm font-typewriter text-amber-400 tracking-widest font-semibold uppercase flex items-center gap-2 drop-shadow-[0_2px_4px_rgba(0,0,0,1)]">
                            <span class="w-2 h-2 rounded-full bg-amber-400 shadow-[0_0_8px_rgba(245,158,11,1)]"></span>
                            <span id="prologueEraText">1885 – 1908 • ĐÊM DÀI NÔ LỆ</span>
                        </span>
                        
                        <div class="flex items-center gap-1.5" id="prologueDots">
                            <span class="w-7 h-1 rounded-full bg-amber-400 shadow-[0_0_8px_rgba(245,158,11,1)]"></span>
                            <span class="w-2.5 h-1 rounded-full bg-white/40"></span>
                            <span class="w-2.5 h-1 rounded-full bg-white/40"></span>
                        </div>
                    </div>

                    <h2 id="prologueTitle" class="text-xl md:text-3xl lg:text-4xl font-bold font-cinematic text-white tracking-wide leading-tight drop-shadow-[0_3px_12px_rgba(0,0,0,1)]">
                        Tiếng súng Cần Vương tắt lịm, Phong trào Đông Du tan vỡ
                    </h2>

                    <p id="prologueSubtext" class="text-sm md:text-lg font-cinematic italic text-amber-200 leading-snug drop-shadow-[0_2px_8px_rgba(0,0,0,1)] max-w-3xl">
                        "‘Đuổi hổ cửa trước rước beo cửa sau’ — Mọi con đường cũ đều bế tắc."
                    </p>

                    <div class="flex items-center justify-between pt-3">
                        <button id="btnProloguePrev" onclick="event.stopPropagation(); prevPrologueSlide()" class="min-h-[44px] px-4 py-2 rounded-xl border border-white/20 bg-black/40 hover:bg-black/70 backdrop-blur-sm text-slate-300 hover:text-white text-xs font-typewriter transition-all flex items-center gap-2 opacity-30 pointer-events-none cursor-pointer">
                            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
                            <span>Trước</span>
                        </button>

                        <div class="flex items-center gap-3">
                            <span class="text-xs text-slate-300/80 font-typewriter hidden sm:inline drop-shadow-[0_1px_3px_rgba(0,0,0,1)]">Nhấp màn hình / Phím [Space] để tiếp tục</span>
                            <button id="btnPrologueNext" onclick="event.stopPropagation(); nextPrologueSlide()" class="min-h-[44px] px-6 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-black font-cinematic font-bold text-xs md:text-sm tracking-wider uppercase transition-all shadow-[0_0_30px_rgba(245,158,11,0.6)] flex items-center gap-2 cursor-pointer">
                                <span id="btnPrologueNextText">Tiếp Tục [Space] →</span>
                                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- TƯƠNG TÁC 1: QUẸT DIÊM VẬT LÝ KHỞI ĐẦU (MATCH RITUAL) -->
        <!-- ======================================================== -->
        <div id="matchRitualStage" class="hidden absolute inset-0 z-50 bg-black/95 backdrop-blur-md flex flex-col items-center justify-between p-6 transition-opacity duration-1000 overflow-hidden">
            <canvas id="sparkCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-20"></canvas>

            <div class="text-center pt-4 z-10">
                <span class="inline-block px-3 py-1 rounded-full bg-brass/10 border border-brass/40 text-brass text-[11px] font-cinematic uppercase tracking-widest mb-1.5">
                    Nghi Thức Vật Lý Khởi Đầu
                </span>
                <h2 class="text-2xl md:text-3xl font-bold font-cinematic text-slate-100 tracking-wide">
                    Cầm Que Diêm Quẹt Lửa & Thắp Đèn Dầu 1911
                </h2>
                <p id="matchHintText" class="text-xs md:text-sm text-amber-300/90 max-w-lg mx-auto mt-1 font-light leading-relaxed">
                    1. Nhấp giữ chuột vào <strong>Que Diêm Gỗ</strong>.<br>
                    2. Kéo quẹt mạnh đầu diêm qua <strong>Dải Nhám Nâu</strong> ở cạnh hộp diêm để đánh lửa!
                </p>
            </div>

            <!-- Matchbox & Draggable Matchstick Area -->
            <div id="tableSurface" class="relative w-full max-w-2xl h-80 flex items-center justify-center z-10">
                <!-- Vintage Matchbox -->
                <div id="vintageMatchbox" 
                     class="relative w-64 h-40 bg-gradient-to-br from-[#4a3525] via-[#332215] to-[#24170d] rounded-xl border-2 border-[#8c6d48] shadow-[0_20px_50px_rgba(0,0,0,0.9)] flex items-center justify-between p-3 select-none">
                    
                    <div class="flex-1 h-full border border-[#8c6d48]/50 rounded-lg p-2.5 flex flex-col justify-between bg-[#291b10]/60">
                        <div class="flex items-center justify-between border-b border-[#8c6d48]/40 pb-1">
                            <span class="text-[9px] font-cinematic uppercase text-amber-400 font-bold tracking-widest">Sài Gòn 1911</span>
                            <span class="text-[9px] font-typewriter text-slate-400">N° 05</span>
                        </div>
                        <div class="text-center py-1">
                            <h4 class="font-cinematic text-sm font-bold text-amber-200 uppercase tracking-widest leading-tight">DIÊM BẾN THÀNH</h4>
                            <p class="text-[8px] font-typewriter text-amber-500/80 mt-0.5">FABRICATION INDOCHINE</p>
                            <svg class="w-5 h-5 text-amber-400 mx-auto mt-1" viewBox="0 0 24 24" fill="currentColor">
                                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                            </svg>
                        </div>
                        <div class="text-[8px] text-slate-500 font-typewriter text-center border-t border-[#8c6d48]/40 pt-1">
                            BẢO ĐẢM NHẠY LỬA
                        </div>
                    </div>

                    <!-- Striker Strip -->
                    <div id="strikerStrip" 
                         class="w-10 h-full ml-3 rounded striker-strip border border-[#59351e] flex flex-col items-center justify-center relative cursor-crosshair group">
                        <span class="text-[8px] font-typewriter text-amber-200/80 uppercase font-bold tracking-tighter transform -rotate-90 whitespace-nowrap pointer-events-none">
                            DẢI QUẸT DIÊM
                        </span>
                        <div class="absolute inset-0 border border-amber-400/60 rounded animate-pulse pointer-events-none"></div>
                    </div>
                </div>

                <!-- Draggable Matchstick -->
                <div id="draggableMatchstick" 
                     class="absolute top-1/2 left-[15%] -translate-y-1/2 w-44 h-8 flex items-center cursor-grab active:cursor-grabbing transition-transform select-none z-30"
                     style="transform: rotate(-15deg); touch-action: none;">
                    
                    <div class="w-36 h-2.5 bg-gradient-to-r from-[#d9be9b] to-[#c29f74] rounded-l-sm border-t border-b border-[#9c7a52] shadow-md relative">
                        <div class="absolute inset-0 bg-black/10"></div>
                    </div>
                    
                    <div id="matchHead" 
                         class="relative w-6 h-4 -ml-1 rounded-full bg-gradient-to-r from-red-600 to-red-800 border border-red-500 shadow-[0_0_8px_rgba(220,38,38,0.8)] flex items-center justify-center">
                        <div id="matchFlame" class="hidden absolute -top-9 left-1 w-6 h-10 pointer-events-none">
                            <svg class="w-full h-full filter drop-shadow-[0_0_12px_rgba(245,158,11,1)] animate-pulse" viewBox="0 0 30 50" fill="none">
                                <path d="M15,0 Q24,20 18,35 Q15,45 8,35 Q0,20 15,0 Z" fill="#f59e0b"/>
                                <path d="M15,10 Q20,25 16,35 Q14,40 10,35 Q5,25 15,10 Z" fill="#fde047"/>
                                <circle cx="15" cy="36" r="4" fill="#ffffff"/>
                            </svg>
                        </div>
                    </div>

                    <span id="matchGrabLabel" class="absolute -bottom-5 left-4 text-[9px] text-amber-300 font-typewriter bg-void/80 px-2 py-0.5 rounded border border-brass/30 pointer-events-none">
                        Nhấp giữ để cầm que diêm
                    </span>
                </div>

                <!-- Target Kerosene Lamp -->
                <div id="targetLanternRitual" class="absolute top-1/2 right-[6%] -translate-y-1/2 flex flex-col items-center pointer-events-auto">
                    <div class="relative w-20 h-32 flex items-center justify-center">
                        <div id="ritualLanternAura" class="absolute inset-0 rounded-full border-2 border-dashed border-amber-400 animate-spin-slow"></div>
                        <svg class="w-16 h-28 text-amber-500 filter drop-shadow-[0_0_15px_rgba(245,158,11,0.6)]" viewBox="0 0 60 100" fill="none">
                            <path d="M30,10 C15,10 10,25 10,35 L50,35 C50,25 45,10 30,10 Z" stroke="#8c6d3b" stroke-width="3" fill="#2d2212"/>
                            <rect x="22" y="2" width="16" height="10" rx="2" fill="#a48147"/>
                            <ellipse cx="30" cy="55" rx="18" ry="24" fill="rgba(245, 158, 11, 0.3)" stroke="#c29953" stroke-width="2"/>
                            <rect id="ritualWick" x="28" y="52" width="4" height="10" fill="#332211"/>
                            <path d="M12,78 L48,78 L44,95 L16,95 Z" fill="#4a3921" stroke="#8c6d3b" stroke-width="2"/>
                        </svg>
                    </div>
                    <span class="text-[10px] text-amber-300 font-typewriter uppercase mt-1 tracking-wider">
                        Đèn Dầu (Mục Tiêu)
                    </span>
                </div>
            </div>

            <div class="text-center pb-3 z-10">
                <button onclick="skipMatchRitual()" 
                        class="text-[11px] text-slate-400 hover:text-amber-300 underline font-typewriter cursor-pointer transition-colors">
                    Bỏ qua nghi thức kéo thả (Thắp sáng đèn ngay)
                </button>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- TƯƠNG TÁC 3: SỔ THUYỀN VIÊN 1911 (CREW REGISTER MODAL) -->
        <!-- ======================================================== -->
        <div id="crewRegisterModal" class="hidden absolute inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
            <div class="max-w-2xl w-full bg-[#1e1712] border-2 border-[#8c6d48] rounded-xl p-6 shadow-[0_25px_60px_rgba(0,0,0,0.95)] flex flex-col text-slate-200 relative select-none">
                <!-- French-Indochina Header -->
                <div class="text-center border-b border-[#8c6d48]/50 pb-4 mb-4">
                    <span class="text-[10px] uppercase font-typewriter text-amber-500 tracking-widest block">
                        COMPAGNIE DES CHARGEURS RÉUNIS • SAÏGON
                    </span>
                    <h3 class="font-cinematic text-lg md:text-xl font-bold text-amber-200 uppercase tracking-wider mt-1">
                        Sổ Thuyền Viên Tàu Amiral Latouche-Tréville (1911)
                    </h3>
                    <p class="text-xs text-slate-400 font-typewriter mt-0.5">
                        Registre d'Équipage — Tuyển Mộ Nhân Lực Chuyến Hải Trình Đại Tây Dương
                    </p>
                </div>

                <!-- Ledger Table -->
                <div class="space-y-3 font-typewriter text-xs flex-1">
                    <!-- Row 1: Văn Ba -->
                    <div class="p-3 rounded bg-[#2b2118] border border-[#8c6d48]/40 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <div>
                            <span class="text-[10px] text-amber-400 uppercase font-bold block">Thuyền viên số 01:</span>
                            <span class="text-sm font-bold text-amber-100 font-cinematic">VĂN BA</span>
                            <span class="text-slate-400 block sm:inline sm:ml-2">(Nguyễn Tất Thành • 21 tuổi)</span>
                        </div>
                        <div class="text-right">
                            <span class="text-amber-300 font-semibold">Aide-cuisinier (Phụ Bếp)</span>
                            <span class="text-[10px] text-slate-400 block">Lương: 45 Francs / tháng</span>
                        </div>
                    </div>

                    <!-- Row 2: Player's Row -->
                    <div class="p-3 rounded bg-[#362a1e] border-2 border-dashed border-amber-500/70 flex flex-col gap-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] text-amber-300 uppercase font-bold flex items-center gap-1.5">
                                <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
                                Thuyền viên số 02 (Người bạn đồng hành tri kỷ):
                            </span>
                            <span class="text-[10px] text-amber-400 font-bold uppercase">Aide-cuisinier (Phụ Bếp)</span>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                            <div>
                                <label class="text-[10px] text-slate-400 uppercase block mb-1">Họ Tên Của Bạn:</label>
                                <input id="regPlayerName" type="text" value="Nguyễn Văn Đồng Hành" 
                                       class="w-full bg-[#1a140f] border border-[#8c6d48] rounded px-3 py-1.5 text-amber-200 font-typewriter text-xs focus:outline-none focus:border-amber-400">
                            </div>
                            <div>
                                <label class="text-[10px] text-slate-400 uppercase block mb-1">Tuổi Của Bạn:</label>
                                <input id="regPlayerAge" type="number" value="21" 
                                       class="w-full bg-[#1a140f] border border-[#8c6d48] rounded px-3 py-1.5 text-amber-200 font-typewriter text-xs focus:outline-none focus:border-amber-400">
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Red Wax Stamp Action Button -->
                <div class="mt-5 pt-4 border-t border-[#8c6d48]/50 flex flex-col sm:flex-row items-center justify-between gap-3">
                    <span class="text-[11px] text-slate-400 font-typewriter">
                        Đóng dấu mộc son xác nhận cùng anh Ba lên tàu vượt biển!
                    </span>
                    <button id="btnSignRegister" onclick="submitCrewRegister()" 
                            class="px-6 py-3 rounded-xl bg-gradient-to-r from-red-700 via-crimson to-red-800 hover:from-red-600 hover:to-red-700 text-white font-cinematic font-bold text-xs uppercase tracking-wider shadow-[0_0_25px_rgba(220,38,38,0.7)] flex items-center gap-2 cursor-pointer transition-transform active:scale-95">
                        <svg class="w-4 h-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/><polygon points="12 8 8 12 16 12 12 8"/></svg>
                        Ký Tên & Đóng Dấu Mộc Son 1911
                    </button>
                </div>

                <!-- Animated Wax Stamp Mark (Appears upon stamp click) -->
                <div id="waxStampMark" class="hidden absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-48 h-48 pointer-events-none transform -rotate-12 z-30">
                    <div class="w-full h-full rounded-full border-4 border-dashed border-red-600 bg-red-800/80 p-2 flex flex-col items-center justify-center text-center shadow-2xl backdrop-blur-sm animate-ping-once">
                        <span class="text-[10px] text-red-200 font-typewriter font-bold uppercase">CHARGEURS RÉUNIS</span>
                        <span class="text-xs font-cinematic text-white font-bold uppercase tracking-wider">ACCEPTÉ • 1911</span>
                        <span class="text-[9px] text-red-300 font-typewriter mt-0.5">SAÏGON - VAPEUR LATOUCHE</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- TƯƠNG TÁC 5: HẦM THAN 40°C (COAL SHOVEL MODAL) -->
        <!-- ======================================================== -->
        <div id="coalShovelModal" class="hidden absolute inset-0 z-50 bg-black/92 backdrop-blur-md flex items-center justify-center p-4">
            <div class="max-w-xl w-full bg-[#171310] border-2 border-orange-700/60 rounded-xl p-6 shadow-2xl flex flex-col items-center select-none">
                <span class="px-3 py-1 rounded-full bg-orange-950/80 border border-orange-500/50 text-orange-400 text-[10px] font-cinematic uppercase tracking-widest mb-2">
                    Lao Động Chân Chính Hầm Tàu 40°C
                </span>
                <h3 class="font-cinematic text-lg md:text-xl font-bold text-orange-200 uppercase tracking-wider text-center">
                    Xúc Than Vào Lò Lửa Hơi Nước
                </h3>
                <p class="text-xs text-slate-300 text-center font-light mt-1 max-w-md">
                    Hãy kéo chiếc xẻng than đổ thẳng vào cửa lò lửa hừng hực để tăng áp suất hơi nước cho con tàu vượt trùng khơi!
                </p>

                <!-- Furnace Door Graphic -->
                <div id="furnaceContainer" class="relative w-64 h-48 bg-stone-900 border-4 border-stone-700 rounded-t-full mt-4 flex items-center justify-center overflow-hidden shadow-inner">
                    <!-- Roaring Fire Flames -->
                    <div class="absolute inset-x-2 bottom-0 h-36 bg-gradient-to-t from-orange-600 via-amber-500 to-transparent rounded-t-full filter blur-xs animate-pulse opacity-90"></div>
                    <div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none z-10">
                        <span class="text-[11px] font-typewriter text-yellow-200 uppercase font-bold tracking-widest drop-shadow-[0_2px_4px_rgba(0,0,0,1)]">
                            CỬA LÒ NÓNG BỎNG
                        </span>
                        <span class="text-[9px] text-orange-200 font-typewriter">Nhiệt độ > 42°C</span>
                    </div>
                </div>

                <!-- Draggable Shovel -->
                <div id="draggableShovel" 
                     class="mt-4 px-6 py-3 rounded-xl bg-stone-800 border-2 border-amber-500/80 cursor-grab active:cursor-grabbing text-amber-300 font-typewriter text-xs uppercase flex items-center gap-2 shadow-lg transition-transform active:scale-95"
                     style="touch-action: none;">
                    <svg class="w-5 h-5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 22l1-1h3l9-9"/><path d="M15 5l4 4"/><path d="M18 2l4 4-2 2-4-4z"/></svg>
                    <span>Kéo Xẻng Than Đổ Vào Lò →</span>
                </div>

                <button onclick="finishCoalShovel()" class="text-slate-500 hover:text-amber-300 text-[11px] font-typewriter mt-4 underline cursor-pointer">
                    Bỏ qua xúc than (Tiếp tục)
                </button>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- TƯƠNG TÁC 6: SỔ TAY TỪ VỰNG TIẾNG PHÁP (FRENCH NOTEBOOK) -->
        <!-- ======================================================== -->
        <div id="frenchNotebookModal" class="hidden absolute inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
            <div class="max-w-xl w-full bg-[#f4ecd8] text-[#2c1d11] border-4 border-[#8c6d48] rounded-xl p-6 shadow-2xl flex flex-col relative select-none">
                <div class="flex items-center justify-between border-b-2 border-[#8c6d48]/40 pb-3 mb-3">
                    <div>
                        <span class="text-[10px] font-typewriter uppercase tracking-widest text-[#8c6d48] font-bold block">
                            ĐÊM TRÊN ĐẠI DƯƠNG • NĂM 1911
                        </span>
                        <h3 class="font-cinematic text-lg md:text-xl font-bold text-[#3a2211]">
                            Sổ Tay Ghi Chép Từ Vựng Của Bác
                        </h3>
                    </div>
                    <span id="notebookPageNum" class="text-xs font-typewriter font-bold bg-[#e5d7ba] px-2.5 py-1 rounded border border-[#8c6d48]/30">
                        Trang 1 / 2
                    </span>
                </div>

                <!-- Handwritten Style Notes -->
                <div id="notebookContent" class="space-y-2.5 font-typewriter text-xs md:text-sm py-2 min-h-[140px]">
                    <div class="p-2 rounded bg-[#ece1c5] border-l-4 border-amber-700">
                        <strong class="text-amber-950 font-bold">la liberté</strong> : Tự do
                    </div>
                    <div class="p-2 rounded bg-[#ece1c5] border-l-4 border-amber-700">
                        <strong class="text-amber-950 font-bold">la patrie</strong> : Tổ quốc, Đất mẹ
                    </div>
                    <div class="p-2 rounded bg-[#ece1c5] border-l-4 border-amber-700">
                        <strong class="text-amber-950 font-bold">l'égalité</strong> : Bình đẳng
                    </div>
                    <div class="p-2 rounded bg-[#ece1c5] border-l-4 border-amber-700">
                        <strong class="text-amber-950 font-bold">la fraternité</strong> : Bác ái, Tình huynh đệ
                    </div>
                </div>

                <div class="mt-4 pt-3 border-t-2 border-[#8c6d48]/40 flex items-center justify-between">
                    <span class="text-[11px] text-[#6b4c30] italic font-cinematic">
                        "Muốn thắng kẻ thù, trước hết phải hiểu ngôn ngữ của chúng."
                    </span>
                    <button id="btnFlipNotebook" onclick="flipNotebookPage()" 
                            class="px-4 py-2 rounded-lg bg-[#3a2211] hover:bg-[#251509] text-amber-200 font-cinematic font-bold text-xs uppercase tracking-wider flex items-center gap-1.5 cursor-pointer shadow">
                        <span>Lật Trang Tiếp Theo</span>
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- TƯƠNG TÁC 7: KÍNH LÚP SOI LUẬN CƯƠNG LÊNIN (MAGNIFIER) -->
        <!-- ======================================================== -->
        <div id="thesisMagnifierModal" class="hidden absolute inset-0 z-50 bg-black/92 backdrop-blur-md flex items-center justify-center p-4">
            <div class="max-w-2xl w-full bg-[#1b1916] border-2 border-brass/60 rounded-xl p-6 shadow-2xl flex flex-col select-none">
                <div class="text-center border-b border-brass/30 pb-3 mb-4">
                    <span class="text-[10px] font-typewriter uppercase tracking-widest text-amber-400 block">
                        PARIS • THÁNG 7 NĂM 1920 • BÁO L'HUMANITÉ
                    </span>
                    <h3 class="font-cinematic text-lg md:text-xl font-bold text-white uppercase tracking-wider mt-1">
                        Sơ Thảo Lần Thứ Nhất Những Luận Cương Của V.I. Lênin
                    </h3>
                </div>

                <!-- Newspaper Replica with Glowing Passage -->
                <div class="p-4 rounded-lg bg-[#29241e] border border-amber-500/40 relative overflow-hidden font-typewriter text-xs leading-relaxed text-slate-300">
                    <p class="opacity-60 mb-2">
                        <em>Premier esquisse des thèses sur les questions nationales et coloniales pour le IIe Congrès de l'Internationale Communiste...</em>
                    </p>
                    <div class="p-3.5 rounded-lg bg-amber-950/70 border-2 border-amber-400/80 text-amber-200 shadow-[0_0_20px_rgba(245,158,11,0.35)]">
                        <span class="text-[10px] text-amber-400 font-bold uppercase tracking-wider block mb-1">
                            ÁNH SÁNG CHÂN LÝ SOi ĐƯỜNG:
                        </span>
                        <p class="font-cinematic text-sm md:text-base text-amber-100 font-semibold leading-snug">
                            "Hỡi đồng bào bị đọa đày đau khổ! Đây là cái cần thiết cho chúng ta, đây là con đường giải phóng chúng ta!"
                        </p>
                        <p class="text-[11px] text-slate-300 mt-1.5 font-light">
                            — Nguyễn Ái Quốc reo to lên một mình trong phòng trọ như nói trước hàng vạn quần chúng nhân dân.
                        </p>
                    </div>
                </div>

                <div class="mt-4 pt-3 border-t border-brass/30 flex items-center justify-between">
                    <span class="text-xs text-slate-400 font-typewriter">
                        Bước ngoặt quyết định đưa Người đến với Chủ nghĩa Mác - Lênin.
                    </span>
                    <button onclick="finishThesisMagnifier()" 
                            class="px-5 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-black font-cinematic font-bold text-xs uppercase tracking-wider shadow-[0_0_20px_rgba(245,158,11,0.6)] cursor-pointer">
                        Đã Thấu Suốt Chân Lý Cứu Nước →
                    </button>
                </div>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- TƯƠNG TÁC 8: SÁCH ĐƯỜNG KÁCH MỆNH 1927 (BOOK MODAL) -->
        <!-- ======================================================== -->
        <div id="duongKachMenhModal" class="hidden absolute inset-0 z-50 bg-black/92 backdrop-blur-md flex items-center justify-center p-4">
            <div class="max-w-xl w-full bg-[#201811] border-2 border-amber-600/70 rounded-xl p-6 shadow-2xl flex flex-col select-none">
                <div class="text-center border-b border-amber-700/50 pb-3 mb-3">
                    <span class="text-[10px] font-typewriter uppercase tracking-widest text-amber-400">
                        QUẢNG CHÂU (TRUNG QUỐC) • NĂM 1925 – 1927
                    </span>
                    <h3 class="font-cinematic text-xl font-bold text-amber-100 tracking-wider mt-1">
                        Tác Phẩm Kinh Điển "ĐƯỜNG KÁCH MỆNH"
                    </h3>
                </div>

                <div class="p-4 rounded-lg bg-[#2e2216] border border-amber-600/40 text-slate-200 font-typewriter text-xs md:text-sm leading-relaxed space-y-2.5">
                    <p class="text-amber-300 font-bold uppercase text-xs">
                        Tư tưởng then chốt của Nguyễn Ái Quốc:
                    </p>
                    <blockquote class="italic font-cinematic text-sm md:text-base text-amber-100 border-l-4 border-amber-500 pl-3 py-1">
                        "Cách mệnh trước hết phải có cái gì? Trước hết phải có Đảng cách mệnh, để trong thì vận động và tổ chức dân chúng, ngoài thì liên lạc với dân tộc bị áp bức và vô sản giai cấp mọi nơi. Đảng có vững cách mệnh mới thành công, cũng như người cầm lái có vững thuyền mới chạy."
                    </blockquote>
                    <p class="text-[11px] text-slate-400">
                        — Xuất bản năm 1927, làm cơ sở chính trị và tư tưởng cho sự ra đời của Đảng Cộng sản Việt Nam (1930).
                    </p>
                </div>

                <div class="mt-4 pt-3 border-t border-amber-700/50 flex justify-end">
                    <button onclick="finishDuongKachMenh()" 
                            class="px-5 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-black font-cinematic font-bold text-xs uppercase tracking-wider shadow cursor-pointer">
                        Tiếp Tục Tiến Bước Lịch Sử →
                    </button>
                </div>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- TƯƠNG TÁC 9: CHẠM CỘT MỐC 108 PÁC BÓ (MILESTONE TOUCH) -->
        <!-- ======================================================== -->
        <div id="milestone108Modal" class="hidden absolute inset-0 z-50 bg-black/92 backdrop-blur-md flex items-center justify-center p-4">
            <div class="max-w-xl w-full bg-[#18191c] border-2 border-emerald-600/60 rounded-xl p-6 shadow-2xl flex flex-col items-center select-none text-center">
                <span class="px-3 py-1 rounded-full bg-emerald-950/80 border border-emerald-500/50 text-emerald-300 text-[10px] font-cinematic uppercase tracking-widest mb-2">
                    Mùa Xuân Năm 1941 • 30 Năm Trở Về
                </span>
                <h3 class="font-cinematic text-xl font-bold text-white uppercase tracking-wider">
                    Cột Mốc 108 — Thiêng Liêng Đất Mẹ Pác Bó
                </h3>
                <p class="text-xs text-slate-300 font-light mt-1 max-w-md">
                    Nhấp chạm vào Cột Mốc Biên Giới 108 để cảm nhận hơi ấm thiêng liêng sau 30 năm bôn ba trở về Tổ quốc!
                </p>

                <!-- Milestone Graphic -->
                <div id="milestoneTarget" onclick="touchMilestoneSuccess()" 
                     class="my-4 w-36 h-48 rounded-t-2xl bg-stone-700 border-4 border-stone-500 flex flex-col items-center justify-center cursor-pointer hover:border-amber-400 hover:scale-105 transition-all shadow-[0_0_30px_rgba(0,0,0,0.9)] group">
                    <span class="text-xl font-bold font-typewriter text-amber-300 group-hover:text-amber-200">108</span>
                    <span class="text-[10px] font-typewriter text-slate-300 uppercase mt-1">VIỆT NAM</span>
                    <span class="text-[9px] text-amber-400/80 mt-2 font-typewriter animate-pulse">Nhấp Chạm →</span>
                </div>

                <p id="cheLanVienPoem" class="hidden font-cinematic italic text-xs md:text-sm text-amber-200 max-w-md mt-1 animate-fade-in">
                    "Kìa, bóng Bác đang hôn lên hòn đá<br>
                    Lắng nghe trong màu hồng sắc đỏ quê hương..."
                </p>

                <div class="mt-4 pt-3 border-t border-slate-700 w-full flex justify-end">
                    <button id="btnMilestoneNext" onclick="finishMilestone()" 
                            class="px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-black font-cinematic font-bold text-xs uppercase tracking-wider shadow cursor-pointer">
                        Về Hang Cốc Bó Dịch Sử Đảng →
                    </button>
                </div>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- TƯƠNG TÁC 10: VĨ THANH BÌNH MINH ĐỘC LẬP (DAWN BLOOM FINALE) -->
        <!-- ======================================================== -->
        <div id="dawnBloomModal" class="hidden absolute inset-0 z-50 bg-black/95 backdrop-blur-lg flex items-center justify-center p-4">
            <div class="max-w-2xl w-full bg-[#1b150b] border-2 border-amber-400 rounded-2xl p-6 md:p-8 shadow-[0_0_80px_rgba(245,158,11,0.5)] flex flex-col items-center text-center select-none animate-fade-in">
                <span class="px-3.5 py-1.5 rounded-full bg-amber-500/20 border border-amber-400 text-amber-300 text-xs font-cinematic uppercase tracking-widest font-bold mb-3">
                    VĨ THANH KHẢI HOÀN • TƯ TƯỞNG HỒ CHÍ MINH
                </span>
                
                <h2 class="text-2xl md:text-3xl font-bold font-cinematic text-amber-100 tracking-wide leading-tight">
                    Từ Ngọn Đèn Dầu 1911 Đến Bình Minh Độc Lập
                </h2>

                <div class="my-4 p-4 rounded-xl bg-amber-950/40 border border-amber-500/40 max-w-xl text-left font-body text-xs md:text-sm text-slate-200 leading-relaxed">
                    <p class="mb-2">
                        🌟 <strong>Hành trình 30 năm (1911 – 1941)</strong> của Người là minh chứng hùng hồn cho chân lý:
                    </p>
                    <blockquote class="font-cinematic text-sm md:text-base text-amber-200 italic border-l-4 border-amber-400 pl-3 my-2">
                        "Không có gì quý hơn độc lập, tự do!"<br>
                        "Độc lập dân tộc gắn liền với Chủ nghĩa xã hội."
                    </blockquote>
                    <p class="text-slate-400 text-[11px] mt-2 font-typewriter">
                        Ngọn lửa từ căn gác trọ nhỏ năm nào nay đã soi sáng cả non sông gấm vóc Việt Nam hôm nay!
                    </p>
                </div>

                <div class="flex items-center gap-3 mt-2">
                    <button onclick="toggleLogModal(true)" 
                            class="px-5 py-2.5 rounded-xl border border-brass/40 bg-abyss hover:bg-brass/20 text-brass font-cinematic font-bold text-xs uppercase tracking-wider cursor-pointer">
                        Xem Toàn Bộ Nhật Ký Hải Trình
                    </button>
                    <button onclick="restartExperience()" 
                            class="px-6 py-2.5 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-black font-cinematic font-bold text-xs uppercase tracking-wider shadow-[0_0_25px_rgba(245,158,11,0.7)] cursor-pointer">
                        Chơi Lại Từ Đầu [R]
                    </button>
                </div>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- MENU CÁC HỒI KÝ LỊCH SỬ (CHAPTER SELECT MODAL) -->
        <!-- ======================================================== -->
        <div id="chapterMenuModal" class="hidden absolute inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
            <div class="max-w-2xl w-full bg-abyss border border-brass/60 rounded-2xl p-6 flex flex-col shadow-2xl">
                <div class="flex items-center justify-between pb-3 mb-4 border-b border-brass/30">
                    <h3 class="font-cinematic text-lg font-bold text-brass uppercase tracking-wider flex items-center gap-2">
                        <svg class="w-5 h-5 text-brass" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                        Danh Mục 5 Hồi Ký Hải Trình (1911 – 1941)
                    </h3>
                    <button onclick="toggleChapterMenu(false)" class="p-2 text-slate-400 hover:text-white cursor-pointer" aria-label="Đóng">
                        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                    </button>
                </div>

                <div class="space-y-2.5 font-typewriter text-xs overflow-y-auto max-h-[60vh] pr-1">
                    <button onclick="jumpToChapter('prologue')" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 0 • KHỞI NGUỒN TƯ TƯỞNG (1885 – 1911)</span>
                            <span class="text-slate-400 text-[11px]">Đêm Dài Nô Lệ & Lối Rẽ Sang Phương Tây</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter(0)" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 1 • LỜI THỀ GÁC TRỌ (06/1911)</span>
                            <span class="text-slate-400 text-[11px]">Căn Gác Trọ Sài Gòn, Hai Bàn Tay & Cái Bắt Tay Ước Hẹn</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter(4)" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 2 • XUẤT BẾN BẾN NHÀ RỒNG (05.06.1911)</span>
                            <span class="text-slate-400 text-[11px]">Ký Sổ Thuyền Viên Phụ Bếp & Còi Tàu Nhổ Neo</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter(7)" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 3 • GIAN LAO HẢI TRÌNH ĐẠI DƯƠNG (1911 – 1917)</span>
                            <span class="text-slate-400 text-[11px]">Lao Động Hầm Than 40°C & Sổ Tay Từ Vựng Giữa Đại Dương</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter(11)" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 4 • TỎA SÁNG CHÂN LÝ (1920 – 1930)</span>
                            <span class="text-slate-400 text-[11px]">Luận Cương Lênin (Paris) • Đường Kách Mệnh • Thành Lập Đảng</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter(15)" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 5 • TƯƠNG LAI RỰC RỠ (1941)</span>
                            <span class="text-slate-400 text-[11px]">Trở Về Pác Bó, Bàn Đá Cốc Bó & Bình Minh Độc Lập</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- Ý TƯỞNG 1: THẤU KÍNH XUYÊN THỜI GIAN (1911 vs 2026) -->
        <!-- ========================================== -->
        <div id="timeLensContainer" class="hidden absolute inset-0 pointer-events-none z-30">
            <div id="lensCursor" class="absolute w-72 h-72 -translate-x-1/2 -translate-y-1/2 rounded-full overflow-hidden lens-ring pointer-events-none">
                <div class="relative w-full h-full bg-slate-900 overflow-hidden">
                    <svg class="w-full h-full" viewBox="0 0 300 300" fill="none">
                        <rect width="300" height="300" fill="#060c1c"/>
                        <polygon points="140,260 145,40 155,40 160,260" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                        <line x1="150" y1="40" x2="150" y2="15" stroke="#38bdf8" stroke-width="2"/>
                        <circle cx="150" cy="15" r="3" fill="#ef4444" class="animate-ping"/>
                        
                        <rect x="70" y="120" width="35" height="140" fill="#0f172a" stroke="#0ea5e9" stroke-width="1"/>
                        <rect x="110" y="100" width="25" height="160" fill="#1e293b" stroke="#0284c7" stroke-width="1"/>
                        <rect x="165" y="90" width="30" height="170" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
                        <rect x="200" y="130" width="40" height="130" fill="#1e293b" stroke="#0ea5e9" stroke-width="1"/>
                        
                        <path d="M0,230 Q150,220 300,235 L300,300 L0,300 Z" fill="#071b33"/>
                        <line x1="20" y1="250" x2="80" y2="250" stroke="#06b6d4" stroke-width="2" opacity="0.6"/>
                        <line x1="120" y1="260" x2="200" y2="260" stroke="#38bdf8" stroke-width="2" opacity="0.8"/>
                    </svg>

                    <div class="absolute top-3 left-1/2 -translate-x-1/2 px-2.5 py-0.5 rounded-full bg-slate-950/80 border border-cyan-400/50 text-[10px] text-cyan-300 font-typewriter font-bold tracking-widest uppercase flex items-center gap-1.5 shadow-md">
                        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
                        SÀI GÒN 2026 (115 NĂM SAU)
                    </div>
                </div>
            </div>

            <div class="absolute bottom-24 left-1/2 -translate-x-1/2 px-5 py-2.5 rounded-xl bg-void/90 border border-brass/50 backdrop-blur-md text-center max-w-lg shadow-2xl">
                <span class="text-xs font-cinematic font-bold text-amber-300 uppercase tracking-widest">Lát Cắt Lịch Sử 115 Năm</span>
                <p class="text-[12px] text-slate-300 mt-0.5 leading-snug">
                    Từ bến cảng cô đơn năm 1911 nơi người thanh niên áo vải dấn thân vào đêm đen, 
                    nay đã bừng sáng một <strong class="text-cyan-300 font-semibold">Thành phố mang tên Bác</strong> phồn vinh và độc lập!
                </p>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- DIALOGUE LOG MODAL -->
        <!-- ========================================== -->
        <div id="logModal" class="hidden absolute inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-6">
            <div class="max-w-2xl w-full max-h-[80vh] bg-abyss border border-brass/50 rounded-2xl p-6 flex flex-col shadow-2xl">
                <div class="flex items-center justify-between pb-4 border-b border-brass/30">
                    <h3 class="font-cinematic text-lg font-bold text-brass uppercase tracking-wider flex items-center gap-2">
                        <svg class="w-5 h-5 text-brass" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                        Nhật Ký Hải Trình (Dialogue History)
                    </h3>
                    <button onclick="toggleLogModal(false)" class="p-2 rounded hover:bg-slate-800 text-slate-400 hover:text-white cursor-pointer" aria-label="Đóng">
                        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                    </button>
                </div>
                <div id="logContainer" class="flex-1 overflow-y-auto py-4 space-y-4 pr-2 text-sm"></div>
                <div class="pt-3 border-t border-slate-800 text-right">
                    <button onclick="toggleLogModal(false)" class="px-5 py-2 rounded-lg bg-brass/20 border border-brass/40 text-brass text-xs font-semibold uppercase hover:bg-brass/30 cursor-pointer">
                        Quay Lại Sân Khấu (Phím Esc)
                    </button>
                </div>
            </div>
        </div>

    </div>

    <!-- ======================================================== -->
    <!-- JAVASCRIPT: THE COMPLETE 5-ACT CINEMATIC MASTER ENGINE -->
    <!-- ======================================================== -->
    <script>
        /* ----------------------------------------------------
         * 1. 5-ACT MASTER SEQUENTIAL SCRIPT (18 STEPS)
         * ---------------------------------------------------- */
        const SCENE_SCRIPT = [
            // --- HỒI 1: LỜI THỀ GÁC TRỌ (SÀI GÒN, ĐẦU THÁNG 6/1911) ---
            {
                id: 'inn_1',
                image: 'inn_1_talking.jpg',
                act: 'HỒI 1 • LỜI THỀ GÁC TRỌ',
                actIndex: 1,
                sceneNum: 'Cảnh 1/3',
                location: 'Căn Gác Trọ Nhỏ — Sài Gòn',
                coords: '10°46\'N 106°42\'E • Đầu Tháng 06/1911 (Đêm)',
                speaker: 'Người Dẫn Truyện',
                role: 'Căn gác trọ nghèo Sài Gòn • Tháng 6/1911',
                text: 'Đêm sâu trong căn gác trọ nhỏ ở Sài Gòn... Bên chiếc bàn gỗ mộc, ngọn đèn dầu le lói hắt ánh vàng ấm áp lên vách nứa. Chàng thanh niên Nguyễn Tất Thành 21 tuổi ngồi đối diện bạn, đôi mắt sáng quắc tràn đầy chí hướng cứu nước.',
                action: 'ambient'
            },
            {
                id: 'inn_1_dialogue',
                image: 'inn_1_talking.jpg',
                act: 'HỒI 1 • LỜI THỀ GÁC TRỌ',
                actIndex: 1,
                sceneNum: 'Cảnh 1/3',
                location: 'Căn Gác Trọ Nhỏ — Sài Gòn',
                coords: '10°46\'N 106°42\'E • Đầu Tháng 06/1911 (Đêm)',
                speaker: 'Văn Ba',
                role: 'Nguyễn Tất Thành (21 tuổi)',
                text: 'Tôi muốn đi ra nước ngoài, xem nước Pháp và các nước khác. Sau khi xem xét họ làm như thế nào, tôi sẽ trở về giúp đồng bào chúng ta... Anh có dám cùng tôi đi chuyến này không?',
                isChoice: true,
                choices: [
                    {
                        key: '1',
                        label: 'Tôi quyết đi cùng anh! Nhưng sang đó, ta lấy tiền đâu mà sống giữa đất khách quê người?',
                        nextId: 'inn_2',
                        resonanceGain: 25
                    },
                    {
                        key: '2',
                        label: 'Đại dương mênh mông, gian nan muôn trùng... Anh Ba thật sự không sợ hiểm nguy sao?',
                        nextId: 'inn_2',
                        resonanceGain: 25
                    }
                ]
            },
            {
                id: 'inn_2',
                image: 'inn_2_hands.jpg',
                act: 'HỒI 1 • LỜI THỀ GÁC TRỌ',
                actIndex: 1,
                sceneNum: 'Cảnh 2/3',
                location: 'Căn Gác Trọ Nhỏ — Sài Gòn',
                coords: '10°46\'N 106°42\'E • Đầu Tháng 06/1911 (Đêm)',
                speaker: 'Văn Ba',
                role: 'Xòe rộng hai bàn tay rắn rỏi trước ngọn đèn dầu',
                text: 'Đây, tiền đây! Chúng ta sẽ làm việc. Chúng ta sẽ làm bất cứ việc gì để sống và để đi. Hai bàn tay này sẽ nuôi sống chúng ta, anh đừng lo lắng! Có lao động, có ý chí thì không gì là không thể vượt qua.',
                action: 'pledge_drag_trigger'
            },
            {
                id: 'inn_3',
                image: 'inn_3_handshake.jpg',
                act: 'HỒI 1 • LỜI THỀ GÁC TRỌ',
                actIndex: 1,
                sceneNum: 'Cảnh 3/3',
                location: 'Căn Gác Trọ Nhỏ — Sài Gòn',
                coords: '10°46\'N 106°42\'E • Rạng Sáng 05.06.1911',
                speaker: 'Người Dẫn Truyện',
                role: 'Khoảnh khắc ước hẹn lịch sử',
                text: 'Hai bàn tay siết chặt nhau qua ánh đèn dầu bập bùng. Lời thề son sắt giữa hai người thanh niên yêu nước đã được kết giao trong đêm tối thuộc địa. Bình minh đã hé, bến cảng Sài Gòn đang đón đợi!',
                action: 'pledge_confirmed'
            },

            // --- HỒI 2: XUẤT BẾN BẾN NHÀ RỒNG (12H TRƯA 05.06.1911) ---
            {
                id: 'dock_1',
                image: 'dock_1_ship.jpg',
                act: 'HỒI 2 • XUẤT BẾN BẾN NHÀ RỒNG',
                actIndex: 2,
                sceneNum: 'Cảnh 1/3',
                location: 'Bến Nhà Rồng — Cảng Sài Gòn',
                coords: '10°46\'N 106°42\'E • Đúng 12:00 Trưa 05.06.1911',
                speaker: 'Người Dẫn Truyện',
                role: 'Bến cảng Sài Gòn • 12h trưa 05.06.1911',
                text: 'Trưa ngày 5 tháng 6 năm 1911, ánh nắng gay gắt chiếu rọi mặt nước sông Sài Gòn. Trước mắt bạn, con tàu buôn Amiral Latouche-Tréville to lớn sừng sững, hai ống khói đen khổng lồ đang phì phì xả khói than mù mịt chuẩn bị nhổ neo.',
                action: 'dock_smoke'
            },
            {
                id: 'dock_2',
                image: 'dock_2_register.jpg',
                act: 'HỒI 2 • XUẤT BẾN BẾN NHÀ RỒNG',
                actIndex: 2,
                sceneNum: 'Cảnh 2/3',
                location: 'Bàn Thư Ký Hãng Chargeurs Réunis',
                coords: 'Cảng Sài Gòn • 12:15 Trưa 05.06.1911',
                speaker: 'Văn Ba',
                role: 'Trước bàn thư ký hãng tàu Pháp',
                text: 'Tôi đã xin được việc phụ bếp với mức lương 45 quan Pháp một tháng rồi. Cuốn sổ thuyền viên đang mở sẵn, anh hãy ghi tên mình vào ngay để chúng ta cùng lên tàu!',
                action: 'crew_register_trigger'
            },
            {
                id: 'dock_3',
                image: 'dock_3_gangway.jpg',
                act: 'HỒI 2 • XUẤT BẾN BẾN NHÀ RỒNG',
                actIndex: 2,
                sceneNum: 'Cảnh 3/3',
                location: 'Cầu Tàu Gỗ Lên Boong Tàu',
                coords: 'Sông Sài Gòn • 12:30 Trưa 05.06.1911',
                speaker: 'Người Dẫn Truyện',
                role: 'Cầu tàu gỗ bước lên boong',
                text: 'Hai người xách túi vải bước lên cầu tàu dốc đứng. Đứng trên lan can sắt, anh Ba ngoái đầu nhìn lại bến cảng quê hương lần cuối... Tiếng còi tàu giục giã nhổ neo!',
                action: 'whistle_trigger'
            },

            // --- HỒI 3: GIAN LAO HẢI TRÌNH ĐẠI DƯƠNG (06/1911 – 1917) ---
            {
                id: 'ship_1',
                image: 'ship_1_boiler.jpg',
                act: 'HỒI 3 • GIAN LAO HẢI TRÌNH',
                actIndex: 3,
                sceneNum: 'Cảnh 1/4',
                location: 'Hầm Than Tàu Amiral Latouche-Tréville',
                coords: 'Ấn Độ Dương • Mùa Hè 1911',
                speaker: 'Người Dẫn Truyện',
                role: 'Hầm than tàu hơi nước (Nhiệt độ > 40°C)',
                text: 'Dưới đáy sâu của con tàu sắt, nhiệt độ hầm than vượt quá 40 độ C. Tiếng máy gầm rú đinh tai nhức óc. Bụi than đen bám kín mặt mũi, mồ hôi chảy ròng ròng làm cay xè khóe mắt.',
                action: 'coal_shovel_trigger'
            },
            {
                id: 'ship_1_dialogue',
                image: 'ship_1_boiler.jpg',
                act: 'HỒI 3 • GIAN LAO HẢI TRÌNH',
                actIndex: 3,
                sceneNum: 'Cảnh 2/4',
                location: 'Hầm Than Tàu Amiral Latouche-Tréville',
                coords: 'Ấn Độ Dương • Mùa Hè 1911',
                speaker: 'Văn Ba',
                role: 'Lau vội mồ hôi trên trán bên chảo gang',
                text: 'Làm việc từ 4 giờ sáng đến đêm mịt, rửa nồi, khiêng chảo, xúc than... Nhưng anh thấy không, chỉ có lao động chân chính mới giúp ta hiểu thấu nỗi khổ cực của những người cùng khổ trên khắp thế giới này!',
                action: 'ambient'
            },
            {
                id: 'ship_2',
                image: 'ship_2_study.jpg',
                act: 'HỒI 3 • GIAN LAO HẢI TRÌNH',
                actIndex: 3,
                sceneNum: 'Cảnh 3/4',
                location: 'Góc Boong Tàu Ban Đêm',
                coords: 'Giữa Đại Dương Mênh Mông • Đêm Khuya 1911',
                speaker: 'Người Dẫn Truyện',
                role: 'Góc boong tàu đêm khuya',
                text: 'Khi mọi người đã chìm vào giấc ngủ sau một ngày kiệt sức, dưới ánh đèn bão chập chờn che chắn gió biển, anh Ba lại cặm cụi ngồi học, tay cầm mẩu bút chì ghi chép từng từ vựng.',
                action: 'notebook_trigger'
            },
            {
                id: 'ship_2_dialogue',
                image: 'ship_2_study.jpg',
                act: 'HỒI 3 • GIAN LAO HẢI TRÌNH',
                actIndex: 3,
                sceneNum: 'Cảnh 4/4',
                location: 'Góc Boong Tàu Ban Đêm',
                coords: 'Giữa Đại Dương Mênh Mông • Đêm Khuya 1911',
                speaker: 'Văn Ba',
                role: 'Chỉ tay vào trang sổ tay tiếng Pháp',
                text: 'Muốn đánh đổ kẻ thù thực dân, trước hết ta phải hiểu ngôn ngữ, văn hóa và cách cai trị của chúng. Mỗi ngày học vài từ, viết lên cánh tay khi làm bếp để vừa làm vừa nhẩm thuộc!',
                action: 'ambient'
            },

            // --- HỒI 4: TỎA SÁNG CHÂN LÝ — PARIS, QUẢNG CHÂU, HƯƠNG CẢNG (1920 – 1930) ---
            {
                id: 'act4_1',
                image: 'act4_1_paris_lenin.jpg',
                act: 'HỒI 4 • TỎA SÁNG CHÂN LÝ',
                actIndex: 4,
                sceneNum: 'Cảnh 1/4',
                location: 'Ngõ Compoint, Quận 17, Paris',
                coords: 'Paris (Pháp) • Tháng 7/1920 (Mùa Hè)',
                speaker: 'Người Dẫn Truyện',
                role: 'Căn phòng trọ nhỏ ngõ Compoint',
                text: 'Trong căn phòng trọ nhỏ lạnh giá ở Paris, dưới ánh đèn bàn le lói, người thanh niên yêu nước Nguyễn Ái Quốc run run lật từng trang báo L’Humanité đăng "Sơ thảo lần thứ nhất những luận cương về vấn đề dân tộc và thuộc địa" của V.I. Lênin.',
                action: 'thesis_magnifier_trigger'
            },
            {
                id: 'act4_1_quote',
                image: 'act4_1_paris_lenin.jpg',
                act: 'HỒI 4 • TỎA SÁNG CHÂN LÝ',
                actIndex: 4,
                sceneNum: 'Cảnh 2/4',
                location: 'Ngõ Compoint, Quận 17, Paris',
                coords: 'Paris (Pháp) • Tháng 7/1920',
                speaker: 'Nguyễn Ái Quốc',
                role: 'Ngồi một mình trong phòng, reo to lên với non sông',
                text: 'Hỡi đồng bào bị đọa đày đau khổ! Đây là cái cần thiết cho chúng ta, đây là con đường giải phóng chúng ta! Luận cương của Lênin làm cho tôi rất cảm động, phấn khởi, sáng tỏ, tin tưởng biết bao!',
                action: 'ambient'
            },
            {
                id: 'act4_2',
                image: 'act4_2_guangzhou_school.jpg',
                act: 'HỒI 4 • TỎA SÁNG CHÂN LÝ',
                actIndex: 4,
                sceneNum: 'Cảnh 3/4',
                location: 'Nhà Số 13 Đường Văn Minh, Quảng Châu',
                coords: 'Quảng Châu (Trung Quốc) • Năm 1925',
                speaker: 'Người Dẫn Truyện',
                role: 'Lớp huấn luyện chính trị thanh niên',
                text: 'Năm 1925 tại Quảng Châu, Bác mở các lớp huấn luyện chính trị cho thanh niên Việt Nam, sáng lập Hội Việt Nam Cách mạng Thanh niên và xuất bản tác phẩm kinh điển "Đường Kách Mệnh" — kim chỉ nam cho phong trào giải phóng dân tộc.',
                action: 'duongkachmenh_trigger'
            },
            {
                id: 'act4_3',
                image: 'act4_3_party_founded.jpg',
                act: 'HỒI 4 • TỎA SÁNG CHÂN LÝ',
                actIndex: 4,
                sceneNum: 'Cảnh 4/4',
                location: 'Cửu Long, Hương Cảng (Hong Kong)',
                coords: 'Hương Cảng • Mùa Xuân Ngày 03.02.1930',
                speaker: 'Người Dẫn Truyện',
                role: 'Hội nghị hợp nhất các tổ chức cộng sản',
                text: 'Mùa xuân 1930, dưới sự chủ trì của đồng chí Nguyễn Ái Quốc, Hội nghị hợp nhất các tổ chức cộng sản đã diễn ra trong một căn phòng bí mật tại Hương Cảng. Đảng Cộng sản Việt Nam ra đời, chấm dứt cuộc khủng hoảng bế tắc về đường lối cứu nước kéo dài nửa thế kỷ!',
                action: 'ambient'
            },

            // --- HỒI 5: TƯƠNG LAI RỰC RỠ — PÁC BÓ & ÁNH BÌNH MINH NON SÔNG (1941) ---
            {
                id: 'act5_1',
                image: 'act5_1_pacbo_return.jpg',
                act: 'HỒI 5 • TƯƠNG LAI RỰC RỠ',
                actIndex: 5,
                sceneNum: 'Cảnh 1/3',
                location: 'Cột Mốc 108 Biên Giới Việt - Trung',
                coords: 'Pác Bó, Hà Quảng, Cao Bằng • 28.01.1941',
                speaker: 'Người Dẫn Truyện',
                role: 'Cột mốc 108 Cao Bằng (Sau 30 năm bôn ba)',
                text: 'Ngày 28 tháng 1 năm 1941 — sau tròn 30 năm bôn ba khắp năm châu bốn biển, Bác Hồ kính yêu đặt bước chân thiêng liêng đầu tiên trở về đất mẹ qua cột mốc 108 Cao Bằng. Người cúi mình nâng niu hòn đá và nắm đất Tổ quốc trong niềm xúc động trào dâng.',
                action: 'milestone_trigger'
            },
            {
                id: 'act5_2',
                image: 'act5_2_pacbo_lamp.jpg',
                act: 'HỒI 5 • TƯƠNG LAI RỰC RỠ',
                actIndex: 5,
                sceneNum: 'Cảnh 2/3',
                location: 'Hang Cốc Bó, Suối Lênin',
                coords: 'Pác Bó, Cao Bằng • Mùa Xuân 1941',
                speaker: 'Người Dẫn Truyện',
                role: 'Bàn đá chông chênh hang Pác Bó',
                text: '"Bàn đá chông chênh dịch sử Đảng / Cuộc đời cách mạng thật là sang". Bên dòng suối Lênin trong vắt, chiếc đèn dầu mộc mạc lại thắp sáng trong hang đá, soi đường cho Hội nghị Trung ương 8 quyết định thành lập Mặt trận Việt Minh, giương cao ngọn cờ độc lập dân tộc.',
                action: 'ambient'
            },
            {
                id: 'act5_3',
                image: 'act5_3_sunrise_independence.jpg',
                act: 'HỒI 5 • TƯƠNG LAI RỰC RỠ',
                actIndex: 5,
                sceneNum: 'Cảnh 3/3',
                location: 'Việt Nam • Độc Lập - Tự Do - Hạnh Phúc',
                coords: 'Mùa Thu Lịch Sử • Quảng Trường Ba Đình',
                speaker: 'Người Dẫn Truyện',
                role: 'Bình minh Độc Lập • Đúc kết Tư tưởng Hồ Chí Minh',
                text: 'Từ ngọn đèn dầu nhỏ nhoi trong căn gác trọ Sài Gòn năm 1911, ngọn lửa yêu nước và ý chí bất khuất đã bùng lên thành Ánh Bình Minh Độc Lập chói lọi! "Không có gì quý hơn độc lập, tự do!" — Tư tưởng Hồ Chí Minh mãi mãi là ngọn hải đăng soi sáng non sông Việt Nam.',
                action: 'dawn_bloom_trigger'
            }
        ];

        /* ----------------------------------------------------
         * 1.5. HỒI 0: DẪN NHẬP LỊCH SỬ (PROLOGUE SLIDES)
         * ---------------------------------------------------- */
        const PROLOGUE_SLIDES = [
            {
                id: 'prologue_1',
                image: 'prologue_1_can_vuong.jpg',
                era: '1885 – 1908 • ĐÊM DÀI NÔ LỆ',
                title: 'Tiếng súng Cần Vương tắt lịm, Phong trào Đông Du tan vỡ',
                subtext: '‘Đuổi hổ cửa trước rước beo cửa sau’ — Mọi con đường cũ đều bế tắc.',
                buttonText: 'Tiếp Tục [Space] →'
            },
            {
                id: 'prologue_2',
                image: 'prologue_2_nguyen_tat_thanh.jpg',
                era: '1910 • TRỰC GIÁC THIÊN TÀI',
                title: 'Không theo lối mòn cũ, Người quyết định đi thẳng sang phương Tây',
                subtext: '‘Đến tận hang ổ của chúng, xem họ làm thế nào rồi trở về giúp đồng bào!’',
                buttonText: 'Đến Bến Sài Gòn [Space] →'
            },
            {
                id: 'prologue_3',
                image: 'prologue_3_saigon_1911.jpg',
                era: 'SÀI GÒN • 05.06.1911',
                title: 'Chàng trai Văn Ba 21 tuổi bước chân xuống bến cảng',
                subtext: 'Bóng tối bao trùm mặt sông, giờ nhổ neo vượt đại dương đã điểm...',
                buttonText: 'QUẸT DIÊM THẮP LỬA ĐẦU TIÊN →'
            }
        ];

        /* ----------------------------------------------------
         * 2. STATE MANAGEMENT
         * ---------------------------------------------------- */
        let state = {
            currentStepIndex: 0,
            activeBgLayer: 'A', // 'A' or 'B'
            isTyping: false,
            typingTimer: null,
            fullText: '',
            audioEnabled: true,
            autoPlay: false,
            autoPlayTimer: null,
            resonance: 25,
            historyLog: [],
            waitingForChoice: false,
            timeLensActive: false,
            isPledgePending: false,
            matchIgnited: false,
            lanternLit: false,
            prologueActive: true,
            prologueIndex: 0,
            playerName: 'Nguyễn Văn Đồng Hành',
            playerAge: 21,
            notebookPage: 1
        };

        /* ----------------------------------------------------
         * 3. PROCEDURAL WEB AUDIO API SYNTHESIZER ENGINE
         * ---------------------------------------------------- */
        let audioCtx = null;
        let ambientGain = null;
        let ambientSource = null;

        function initAudioContext() {
            if (!audioCtx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                audioCtx = new AudioContext();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
        }

        // 3.1. Realistic Ship Horn (3 Sawtooth Oscillators + Filtered Noise Hiss)
        function playShipHorn(customGain = 0.28) {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;

            const t = audioCtx.currentTime;
            const freqs = [108, 136.5, 216];
            const hornMasterGain = audioCtx.createGain();
            hornMasterGain.gain.setValueAtTime(0.001, t);
            hornMasterGain.gain.exponentialRampToValueAtTime(customGain, t + 0.5);
            hornMasterGain.gain.exponentialRampToValueAtTime(customGain * 0.8, t + 2.5);
            hornMasterGain.gain.exponentialRampToValueAtTime(0.0001, t + 4.2);

            freqs.forEach(f => {
                const osc = audioCtx.createOscillator();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(f, t);
                
                const filter = audioCtx.createBiquadFilter();
                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(450, t);
                filter.frequency.exponentialRampToValueAtTime(240, t + 3.8);

                osc.connect(filter);
                filter.connect(hornMasterGain);
                osc.start(t);
                osc.stop(t + 4.2);
            });

            // Steam hiss
            const bufferSize = audioCtx.sampleRate * 2.5;
            const noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
            const data = noiseBuffer.getChannelData(0);
            for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;

            const noiseNode = audioCtx.createBufferSource();
            noiseNode.buffer = noiseBuffer;
            const noiseFilter = audioCtx.createBiquadFilter();
            noiseFilter.type = 'bandpass';
            noiseFilter.frequency.setValueAtTime(1200, t);
            noiseFilter.Q.setValueAtTime(2.0, t);

            const noiseGain = audioCtx.createGain();
            noiseGain.gain.setValueAtTime(0.001, t);
            noiseGain.gain.exponentialRampToValueAtTime(customGain * 0.2, t + 0.3);
            noiseGain.gain.exponentialRampToValueAtTime(0.0001, t + 3.5);

            noiseNode.connect(noiseFilter);
            noiseFilter.connect(noiseGain);
            noiseGain.connect(audioCtx.destination);
            hornMasterGain.connect(audioCtx.destination);

            noiseNode.start(t);
            noiseNode.stop(t + 3.5);
        }

        // 3.2. Real Friction Match Strike Sound
        function playMatchStrikeSound() {
            initAudioContext();
            if (!audioCtx) return;
            const t = audioCtx.currentTime;

            const bSize = audioCtx.sampleRate * 0.16;
            const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;

            const src = audioCtx.createBufferSource();
            src.buffer = buffer;
            const filter = audioCtx.createBiquadFilter();
            filter.type = 'highpass';
            filter.frequency.setValueAtTime(3200, t);

            const gain = audioCtx.createGain();
            gain.gain.setValueAtTime(0.14, t);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.16);

            src.connect(filter);
            filter.connect(gain);
            gain.connect(audioCtx.destination);
            src.start(t);

            const osc = audioCtx.createOscillator();
            const oscGain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(180, t + 0.08);
            osc.frequency.exponentialRampToValueAtTime(65, t + 0.5);

            oscGain.gain.setValueAtTime(0.001, t + 0.08);
            oscGain.gain.exponentialRampToValueAtTime(0.18, t + 0.2);
            oscGain.gain.exponentialRampToValueAtTime(0.0001, t + 0.5);

            osc.connect(oscGain);
            oscGain.connect(audioCtx.destination);
            osc.start(t + 0.08);
            osc.stop(t + 0.5);
        }

        // 3.3. Lever Spring Sound
        function playLeverSpringSound() {
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(540, t);
            osc.frequency.exponentialRampToValueAtTime(180, t + 0.12);

            gain.gain.setValueAtTime(0.05, t);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.12);

            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.start(t);
            osc.stop(t + 0.12);
        }

        // 3.4. Subtle Typewriter Key Sound
        function playTypewriterKey() {
            if (!audioCtx || !state.audioEnabled) return;
            try {
                const t = audioCtx.currentTime;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                const pitch = 1800 + Math.random() * 600;
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(pitch, t);

                gain.gain.setValueAtTime(0.02, t);
                gain.gain.exponentialRampToValueAtTime(0.0001, t + 0.035);

                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start(t);
                osc.stop(t + 0.035);
            } catch (e) {}
        }

        // 3.5. Harmonic Pledge Chime
        function playPledgeChime() {
            initAudioContext();
            if (!audioCtx) return;
            const t = audioCtx.currentTime;
            const chords = [220, 330, 440, 660];
            chords.forEach(f => {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(f, t);
                gain.gain.setValueAtTime(0.001, t);
                gain.gain.exponentialRampToValueAtTime(0.08, t + 0.1);
                gain.gain.exponentialRampToValueAtTime(0.0001, t + 2.8);

                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start(t);
                osc.stop(t + 2.8);
            });
        }

        // 3.6. Heavy Red Wax Stamp Impact Thud
        function playStampSound() {
            initAudioContext();
            if (!audioCtx) return;
            const t = audioCtx.currentTime;

            // Deep wood/brass thud
            const osc = audioCtx.createOscillator();
            const oscGain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(110, t);
            osc.frequency.exponentialRampToValueAtTime(32, t + 0.14);

            oscGain.gain.setValueAtTime(0.35, t);
            oscGain.gain.exponentialRampToValueAtTime(0.001, t + 0.22);

            osc.connect(oscGain);
            oscGain.connect(audioCtx.destination);
            osc.start(t);
            osc.stop(t + 0.22);

            // Paper squelch noise burst
            const bSize = audioCtx.sampleRate * 0.08;
            const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;

            const src = audioCtx.createBufferSource();
            src.buffer = buffer;
            const filter = audioCtx.createBiquadFilter();
            filter.type = 'lowpass';
            filter.frequency.setValueAtTime(380, t);

            const nGain = audioCtx.createGain();
            nGain.gain.setValueAtTime(0.18, t);
            nGain.gain.exponentialRampToValueAtTime(0.001, t + 0.08);

            src.connect(filter);
            filter.connect(nGain);
            nGain.connect(audioCtx.destination);
            src.start(t);
        }

        // 3.7. Roaring Furnace Coal Shovel Sound
        function playFurnaceSound() {
            initAudioContext();
            if (!audioCtx) return;
            const t = audioCtx.currentTime;

            // Metallic shovel scrape
            const osc = audioCtx.createOscillator();
            const oscGain = audioCtx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(680, t);
            osc.frequency.exponentialRampToValueAtTime(220, t + 0.18);

            oscGain.gain.setValueAtTime(0.12, t);
            oscGain.gain.exponentialRampToValueAtTime(0.001, t + 0.25);

            osc.connect(oscGain);
            oscGain.connect(audioCtx.destination);
            osc.start(t);
            osc.stop(t + 0.25);

            // Fire roaring whoosh
            const bSize = audioCtx.sampleRate * 1.4;
            const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;

            const src = audioCtx.createBufferSource();
            src.buffer = buffer;
            const filter = audioCtx.createBiquadFilter();
            filter.type = 'bandpass';
            filter.frequency.setValueAtTime(320, t);
            filter.Q.setValueAtTime(1.5, t);

            const nGain = audioCtx.createGain();
            nGain.gain.setValueAtTime(0.001, t);
            nGain.gain.exponentialRampToValueAtTime(0.24, t + 0.25);
            nGain.gain.exponentialRampToValueAtTime(0.001, t + 1.4);

            src.connect(filter);
            filter.connect(nGain);
            nGain.connect(audioCtx.destination);
            src.start(t);
        }

        // 3.8. Crisp Paper Page Turn Sound
        function playPageTurnSound() {
            initAudioContext();
            if (!audioCtx) return;
            const t = audioCtx.currentTime;

            const bSize = audioCtx.sampleRate * 0.14;
            const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;

            const src = audioCtx.createBufferSource();
            src.buffer = buffer;
            const filter = audioCtx.createBiquadFilter();
            filter.type = 'highpass';
            filter.frequency.setValueAtTime(2400, t);

            const gain = audioCtx.createGain();
            gain.gain.setValueAtTime(0.08, t);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.14);

            src.connect(filter);
            filter.connect(gain);
            gain.connect(audioCtx.destination);
            src.start(t);
        }

        // 3.9. Sacred Border Stone Resonance Chime (Tibetan Singing Bowl Style)
        function playStoneChime() {
            initAudioContext();
            if (!audioCtx) return;
            const t = audioCtx.currentTime;
            const freqs = [216, 432, 648];

            freqs.forEach((f, idx) => {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(f, t);

                const initGain = 0.12 / (idx + 1);
                gain.gain.setValueAtTime(0.001, t);
                gain.gain.exponentialRampToValueAtTime(initGain, t + 0.08);
                gain.gain.exponentialRampToValueAtTime(0.0001, t + 3.6);

                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start(t);
                osc.stop(t + 3.7);
            });
        }

        // 3.10. Triumphant Dawn Bloom Orchestral Major Chord
        function playDawnBloomChord() {
            initAudioContext();
            if (!audioCtx) return;
            const t = audioCtx.currentTime;
            // Majestic C Major Triad swell: C4, G4, C5, E5, G5, C6
            const chord = [261.63, 392.00, 523.25, 659.25, 783.99, 1046.50];

            chord.forEach((f, idx) => {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = idx % 2 === 0 ? 'sine' : 'triangle';
                osc.frequency.setValueAtTime(f, t + idx * 0.06);

                gain.gain.setValueAtTime(0.001, t + idx * 0.06);
                gain.gain.exponentialRampToValueAtTime(0.06, t + 0.8);
                gain.gain.exponentialRampToValueAtTime(0.0001, t + 4.8);

                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start(t + idx * 0.06);
                osc.stop(t + 5.0);
            });
        }

        /* ----------------------------------------------------
         * 3.11. PROLOGUE SOUNDTRACK & MUSIC LOGIC
         * ---------------------------------------------------- */
        let prologueMusicState = {
            isPlaying: false,
            audioElement: null,
            fadeTimer: null,
            pureSineTimer: null,
            pureSineGain: null
        };

        function fadeAudioVolume(audioEl, targetVol, durationMs, onComplete) {
            if (!audioEl) return;
            clearInterval(prologueMusicState.fadeTimer);
            const startVol = audioEl.volume;
            const startTime = performance.now();
            const diff = targetVol - startVol;

            prologueMusicState.fadeTimer = setInterval(() => {
                const elapsed = performance.now() - startTime;
                const progress = Math.min(1, elapsed / durationMs);
                const ease = 1 - Math.pow(1 - progress, 2);
                audioEl.volume = Math.max(0, Math.min(1, startVol + diff * ease));

                if (progress >= 1) {
                    clearInterval(prologueMusicState.fadeTimer);
                    if (onComplete) onComplete();
                }
            }, 30);
        }

        function startPrologueSoundtrack() {
            initAudioContext();
            if (prologueMusicState.isPlaying || !state.audioEnabled) return;
            prologueMusicState.isPlaying = true;

            const hint = document.getElementById('audioStartHint');
            if (hint) hint.classList.add('opacity-0', 'pointer-events-none');

            const audioEl = document.getElementById('prologueBgmAudio');
            prologueMusicState.audioElement = audioEl;

            if (audioEl) {
                audioEl.muted = !state.audioEnabled;
                audioEl.volume = 0;
                const playPromise = audioEl.play();
                if (playPromise !== undefined) {
                    playPromise.then(() => {
                        fadeAudioVolume(audioEl, 0.45, 2400);
                    }).catch(e => {
                        console.info('Acoustic track auto-fallback to Pure Sine warm piano:', e);
                        startPureSineSoundtrack();
                    });
                } else {
                    fadeAudioVolume(audioEl, 0.45, 2400);
                }
            } else {
                startPureSineSoundtrack();
            }
        }

        function stopPrologueSoundtrack(fadeDuration = 1.2) {
            if (!prologueMusicState.isPlaying) return;
            prologueMusicState.isPlaying = false;
            stopPureSineSoundtrack(fadeDuration);

            const audioEl = prologueMusicState.audioElement || document.getElementById('prologueBgmAudio');
            if (audioEl && !audioEl.paused) {
                fadeAudioVolume(audioEl, 0, fadeDuration * 1000, () => {
                    audioEl.pause();
                    audioEl.currentTime = 0;
                });
            }
        }

        function startPureSineSoundtrack() {
            if (!audioCtx || !state.audioEnabled) return;
            try {
                const t = audioCtx.currentTime;
                const pGain = audioCtx.createGain();
                pGain.gain.setValueAtTime(0.001, t);
                pGain.gain.exponentialRampToValueAtTime(0.14, t + 2.0);
                pGain.connect(audioCtx.destination);
                prologueMusicState.pureSineGain = pGain;

                const progression = [
                    [146.83, 174.61, 220.00, 293.66], // Dm
                    [116.54, 174.61, 233.08, 293.66], // Bb
                    [98.00, 146.83, 196.00, 233.08],  // Gm
                    [110.00, 164.81, 220.00, 277.18]  // A
                ];
                let chordStep = 0;

                function playChordArpeggio() {
                    if (!prologueMusicState.isPlaying || !audioCtx) return;
                    const chord = progression[chordStep % progression.length];
                    chordStep++;

                    chord.forEach((freq, idx) => {
                        const noteTime = audioCtx.currentTime + (idx * 0.07);
                        const osc = audioCtx.createOscillator();
                        osc.type = 'sine';
                        osc.frequency.setValueAtTime(freq, noteTime);

                        const gain = audioCtx.createGain();
                        gain.gain.setValueAtTime(0.001, noteTime);
                        gain.gain.exponentialRampToValueAtTime(0.042, noteTime + 0.08);
                        gain.gain.exponentialRampToValueAtTime(0.0001, noteTime + 3.8);

                        osc.connect(gain);
                        gain.connect(pGain);
                        osc.start(noteTime);
                        osc.stop(noteTime + 3.9);
                    });
                }

                playChordArpeggio();
                prologueMusicState.pureSineTimer = setInterval(playChordArpeggio, 4200);
            } catch(e) {}
        }

        function stopPureSineSoundtrack(fadeDuration = 1.2) {
            clearInterval(prologueMusicState.pureSineTimer);
            if (prologueMusicState.pureSineGain && audioCtx) {
                try {
                    const t = audioCtx.currentTime;
                    prologueMusicState.pureSineGain.gain.exponentialRampToValueAtTime(0.0001, t + fadeDuration);
                } catch(e) {}
            }
        }

        /* ----------------------------------------------------
         * 4. PROLOGUE LOGIC
         * ---------------------------------------------------- */
        const pCanvas = document.getElementById('prologueVfxCanvas');
        const pCtx = pCanvas ? pCanvas.getContext('2d') : null;
        let pParticles = [];
        let pAnimFrameId = null;

        function resizePrologueVfx() {
            if (!pCanvas || !pCanvas.parentElement) return;
            pCanvas.width = pCanvas.parentElement.clientWidth || window.innerWidth;
            pCanvas.height = pCanvas.parentElement.clientHeight || window.innerHeight;
            initPrologueParticles();
        }

        function initPrologueParticles() {
            pParticles = [];
            const count = state.prologueIndex === 0 ? 55 : (state.prologueIndex === 1 ? 40 : 35);
            for (let i = 0; i < count; i++) pParticles.push(createPrologueParticle(true));
        }

        function createPrologueParticle(randomY = false) {
            const w = pCanvas ? pCanvas.width : window.innerWidth;
            const h = pCanvas ? pCanvas.height : window.innerHeight;
            const idx = state.prologueIndex;

            if (idx === 0) {
                return {
                    x: Math.random() * (w + 200) - 100,
                    y: randomY ? Math.random() * h : -20,
                    len: Math.random() * 22 + 15,
                    vx: -(Math.random() * 2 + 3),
                    vy: Math.random() * 12 + 18,
                    alpha: Math.random() * 0.35 + 0.15,
                    type: 'rain'
                };
            } else if (idx === 1) {
                return {
                    x: Math.random() * w,
                    y: randomY ? Math.random() * h : h + 15,
                    r: Math.random() * 2.5 + 1.0,
                    vx: (Math.random() - 0.5) * 0.8,
                    vy: -(Math.random() * 0.9 + 0.4),
                    alpha: Math.random() * 0.7 + 0.3,
                    sway: Math.random() * Math.PI * 2,
                    type: 'ember'
                };
            } else {
                return {
                    x: randomY ? Math.random() * w : -80,
                    y: h * 0.55 + Math.random() * (h * 0.45),
                    r: Math.random() * 60 + 35,
                    vx: Math.random() * 0.5 + 0.25,
                    vy: (Math.random() - 0.5) * 0.15,
                    alpha: Math.random() * 0.18 + 0.06,
                    type: 'fog'
                };
            }
        }

        function updatePrologueParticles() {
            if (!state.prologueActive || !pCtx) return;
            const w = pCanvas.width;
            const h = pCanvas.height;
            pCtx.clearRect(0, 0, w, h);

            for (let i = 0; i < pParticles.length; i++) {
                const p = pParticles[i];

                if (p.type === 'rain') {
                    p.x += p.vx;
                    p.y += p.vy;
                    pCtx.strokeStyle = `rgba(180, 210, 240, ${p.alpha})`;
                    pCtx.lineWidth = 1.2;
                    pCtx.beginPath();
                    pCtx.moveTo(p.x, p.y);
                    pCtx.lineTo(p.x + (p.vx * 0.4), p.y + p.len);
                    pCtx.stroke();
                    if (p.y > h || p.x < -50) pParticles[i] = createPrologueParticle(false);
                } else if (p.type === 'ember') {
                    p.sway += 0.03;
                    p.x += p.vx + Math.sin(p.sway) * 0.4;
                    p.y += p.vy;
                    const grad = pCtx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 2);
                    grad.addColorStop(0, `rgba(251, 191, 36, ${p.alpha})`);
                    grad.addColorStop(1, `rgba(245, 158, 11, 0)`);
                    pCtx.fillStyle = grad;
                    pCtx.beginPath();
                    pCtx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    pCtx.fill();
                    if (p.y < -20) pParticles[i] = createPrologueParticle(false);
                } else if (p.type === 'fog') {
                    p.x += p.vx;
                    p.y += p.vy;
                    const grad = pCtx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r);
                    grad.addColorStop(0, `rgba(200, 220, 240, ${p.alpha})`);
                    grad.addColorStop(1, `rgba(200, 220, 240, 0)`);
                    pCtx.fillStyle = grad;
                    pCtx.beginPath();
                    pCtx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    pCtx.fill();
                    if (p.x > w + 100) pParticles[i] = createPrologueParticle(false);
                }
            }

            pAnimFrameId = requestAnimationFrame(updatePrologueParticles);
        }

        function renderPrologueSlide() {
            const slide = PROLOGUE_SLIDES[state.prologueIndex];
            if (!slide) return;

            const bgImg = document.getElementById('prologueBgImg');
            bgImg.className = 'w-full h-full object-cover object-center filter brightness-[0.92] contrast-105 transition-opacity duration-700 transform';
            bgImg.style.opacity = '0.35';
            setTimeout(() => {
                bgImg.src = slide.image;
                bgImg.className = `w-full h-full object-cover object-center filter brightness-[0.92] contrast-105 transition-opacity duration-700 transform kenburns-${state.prologueIndex + 1}`;
                bgImg.style.opacity = '1';
            }, 180);

            document.getElementById('prologueStepIndicator').textContent = `Phân cảnh ${state.prologueIndex + 1} / ${PROLOGUE_SLIDES.length}`;
            document.getElementById('prologueEraText').textContent = slide.era;
            document.getElementById('prologueTitle').textContent = slide.title;
            document.getElementById('prologueSubtext').textContent = `"${slide.subtext}"`;
            document.getElementById('btnPrologueNextText').textContent = slide.buttonText;

            const titleEl = document.getElementById('prologueTitle');
            const subtextEl = document.getElementById('prologueSubtext');
            if (titleEl && subtextEl) {
                titleEl.classList.remove('cinema-title-animate');
                subtextEl.classList.remove('cinema-subtext-animate');
                void titleEl.offsetWidth;
                void subtextEl.offsetWidth;
                titleEl.classList.add('cinema-title-animate');
                subtextEl.classList.add('cinema-subtext-animate');
            }

            initPrologueParticles();
            if (!pAnimFrameId) pAnimFrameId = requestAnimationFrame(updatePrologueParticles);

            const dots = document.getElementById('prologueDots');
            dots.innerHTML = PROLOGUE_SLIDES.map((_, idx) => `
                <span class="${idx === state.prologueIndex ? 'w-7 bg-amber-400 shadow-[0_0_8px_rgba(245,158,11,1)]' : 'w-2.5 bg-white/40'} h-1 rounded-full transition-all duration-300"></span>
            `).join('');

            const btnPrev = document.getElementById('btnProloguePrev');
            if (state.prologueIndex > 0) btnPrev.classList.remove('opacity-30', 'pointer-events-none');
            else btnPrev.classList.add('opacity-30', 'pointer-events-none');

            playTypewriterKey();
        }

        function handlePrologueBackgroundClick(e) {
            if (e.target.closest('button')) return;
            startPrologueSoundtrack();
            nextPrologueSlide();
        }

        function nextPrologueSlide() {
            initAudioContext();
            startPrologueSoundtrack();
            if (state.prologueIndex < PROLOGUE_SLIDES.length - 1) {
                state.prologueIndex++;
                renderPrologueSlide();
            } else {
                finishPrologue();
            }
        }

        function prevPrologueSlide() {
            initAudioContext();
            startPrologueSoundtrack();
            if (state.prologueIndex > 0) {
                state.prologueIndex--;
                renderPrologueSlide();
            }
        }

        function finishPrologue() {
            initAudioContext();
            state.prologueActive = false;
            stopPrologueSoundtrack(1.2);
            if (pAnimFrameId) {
                cancelAnimationFrame(pAnimFrameId);
                pAnimFrameId = null;
            }

            const pStage = document.getElementById('prologueStage');
            pStage.classList.add('opacity-0', 'pointer-events-none');
            playPledgeChime();

            setTimeout(() => {
                pStage.classList.add('hidden');
                // Open Match Ritual
                const matchRitual = document.getElementById('matchRitualStage');
                matchRitual.classList.remove('hidden', 'opacity-0');
            }, 800);
        }

        function skipPrologue() {
            finishPrologue();
        }

        /* ----------------------------------------------------
         * 5. MATCH RITUAL ENGINE (DRAG & STRIKE)
         * ---------------------------------------------------- */
        const matchstick = document.getElementById('draggableMatchstick');
        const matchHead = document.getElementById('matchHead');
        const matchFlame = document.getElementById('matchFlame');
        const strikerStrip = document.getElementById('strikerStrip');
        const targetLanternRitual = document.getElementById('targetLanternRitual');
        const sparkCanvas = document.getElementById('sparkCanvas');
        const sparkCtx = sparkCanvas ? sparkCanvas.getContext('2d') : null;

        let isDraggingMatch = false;
        let matchOffset = { x: 0, y: 0 };
        let lastMatchPos = { x: 0, y: 0, time: 0 };
        let sparks = [];

        function resizeSparkCanvas() {
            if (!sparkCanvas) return;
            sparkCanvas.width = window.innerWidth;
            sparkCanvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeSparkCanvas);
        resizeSparkCanvas();

        function emitSparks(originX, originY, velocityX) {
            for (let i = 0; i < 45; i++) {
                const angle = Math.random() * Math.PI - (Math.PI / 2);
                const speed = Math.random() * 8 + 3;
                sparks.push({
                    x: originX,
                    y: originY,
                    vx: Math.cos(angle) * speed + (velocityX * 0.2),
                    vy: Math.sin(angle) * speed - 2,
                    radius: Math.random() * 2.5 + 1.2,
                    alpha: 1,
                    color: Math.random() > 0.3 ? '#f59e0b' : '#fef08a'
                });
            }
        }

        function updateSparks() {
            if (!sparkCtx) return;
            sparkCtx.clearRect(0, 0, sparkCanvas.width, sparkCanvas.height);
            for (let i = sparks.length - 1; i >= 0; i--) {
                const s = sparks[i];
                s.x += s.vx;
                s.y += s.vy;
                s.vy += 0.25;
                s.alpha -= 0.025;
                if (s.alpha <= 0) {
                    sparks.splice(i, 1);
                    continue;
                }
                sparkCtx.fillStyle = s.color;
                sparkCtx.globalAlpha = s.alpha;
                sparkCtx.beginPath();
                sparkCtx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
                sparkCtx.fill();
            }
            sparkCtx.globalAlpha = 1;
            requestAnimationFrame(updateSparks);
        }
        requestAnimationFrame(updateSparks);

        if (matchstick) {
            matchstick.addEventListener('pointerdown', (e) => {
                initAudioContext();
                isDraggingMatch = true;
                matchstick.setPointerCapture(e.pointerId);
                const rect = matchstick.getBoundingClientRect();
                matchOffset.x = e.clientX - rect.left;
                matchOffset.y = e.clientY - rect.top;
                lastMatchPos = { x: e.clientX, y: e.clientY, time: performance.now() };
                document.getElementById('matchGrabLabel').classList.add('opacity-0');
            });
        }

        window.addEventListener('pointermove', (e) => {
            if (!isDraggingMatch || !matchstick) return;
            const newX = e.clientX - matchOffset.x;
            const newY = e.clientY - matchOffset.y;
            matchstick.style.left = `${newX}px`;
            matchstick.style.top = `${newY}px`;
            matchstick.style.transform = `rotate(${state.matchIgnited ? -25 : -10}deg)`;

            const now = performance.now();
            const dt = now - lastMatchPos.time || 16;
            const dx = e.clientX - lastMatchPos.x;
            const dy = e.clientY - lastMatchPos.y;
            const velocity = Math.hypot(dx, dy) / dt;

            const headRect = matchHead.getBoundingClientRect();
            const strikerRect = strikerStrip.getBoundingClientRect();

            if (!state.matchIgnited) {
                const isOverStriker = (
                    headRect.right >= strikerRect.left &&
                    headRect.left <= strikerRect.right &&
                    headRect.bottom >= strikerRect.top &&
                    headRect.top <= strikerRect.bottom
                );
                if (isOverStriker && velocity > 0.26) {
                    igniteMatchHead(headRect.right, headRect.top + 10, dx);
                }
            } else {
                const lanternRect = targetLanternRitual.getBoundingClientRect();
                const distToLantern = Math.hypot(
                    headRect.left - (lanternRect.left + lanternRect.width / 2),
                    headRect.top - (lanternRect.top + lanternRect.height / 2)
                );
                if (distToLantern < 70) {
                    transferFlameToLantern();
                }
            }
            lastMatchPos = { x: e.clientX, y: e.clientY, time: now };
        });

        window.addEventListener('pointerup', () => {
            if (!isDraggingMatch) return;
            isDraggingMatch = false;
        });

        function igniteMatchHead(sparkX, sparkY, vx) {
            state.matchIgnited = true;
            playMatchStrikeSound();
            emitSparks(sparkX, sparkY, vx);
            matchFlame.classList.remove('hidden');
            document.getElementById('matchHintText').innerHTML = `
                <span class="text-amber-300 font-bold uppercase tracking-wider">Lửa Đã Bén!</span><br>
                Hãy <strong>kéo que diêm đang cháy</strong> chạm vào bấc chiếc Đèn Dầu bên phải!
            `;
            document.getElementById('targetLanternRitual').classList.add('scale-110', 'transition-transform');
        }

        function transferFlameToLantern() {
            if (state.lanternLit) return;
            state.lanternLit = true;
            playMatchStrikeSound();

            const overlay = document.getElementById('matchRitualStage');
            overlay.classList.add('opacity-0', 'pointer-events-none');

            setTimeout(() => {
                overlay.classList.add('hidden');
                state.currentStepIndex = 0;
                renderCurrentStep();
            }, 700);
        }

        function skipMatchRitual() {
            initAudioContext();
            transferFlameToLantern();
        }

        /* ----------------------------------------------------
         * 6. HANDSHAKE DRAG ENGINE (TƯƠNG TÁC 2)
         * ---------------------------------------------------- */
        const compHand = document.getElementById('companionHandDraggable');
        const vanBaTarget = document.getElementById('vanBaHandsTarget');
        let isDraggingHand = false;
        let handStartY = 0;

        if (compHand) {
            compHand.addEventListener('pointerdown', (e) => {
                isDraggingHand = true;
                compHand.setPointerCapture(e.pointerId);
                handStartY = e.clientY;
            });
        }

        window.addEventListener('pointermove', (e) => {
            if (!isDraggingHand || !compHand) return;
            const deltaY = Math.min(0, Math.max(-110, e.clientY - handStartY));
            compHand.style.transform = `translateY(${deltaY}px)`;

            if (deltaY < -75) {
                isDraggingHand = false;
                triggerCompanionHandshakeSuccess();
            }
        });

        window.addEventListener('pointerup', () => {
            if (!isDraggingHand || !compHand) return;
            isDraggingHand = false;
            compHand.style.transition = 'transform 0.25s var(--ease-snap)';
            compHand.style.transform = 'translateY(0px)';
            setTimeout(() => compHand.style.transition = '', 250);
        });

        function triggerCompanionHandshakeSuccess() {
            playPledgeChime();
            state.isPledgePending = false;
            compHand.style.transform = 'translateY(-85px) scale(1.15)';
            if (vanBaTarget) vanBaTarget.classList.add('scale-110');

            state.resonance = Math.min(100, state.resonance + 25);
            updateResonanceHUD();

            setTimeout(() => {
                document.getElementById('pledgeDragContainer').classList.add('hidden');
                state.currentStepIndex = 3; // Advance to inn_3
                renderCurrentStep();
            }, 1000);
        }

        /* ----------------------------------------------------
         * 7. SỔ THUYỀN VIÊN 1911 (TƯƠNG TÁC 3)
         * ---------------------------------------------------- */
        function submitCrewRegister() {
            playStampSound();
            const pName = document.getElementById('regPlayerName').value.trim() || 'Nguyễn Văn Đồng Hành';
            const pAge = document.getElementById('regPlayerAge').value.trim() || '21';
            state.playerName = pName;
            state.playerAge = pAge;

            const stampMark = document.getElementById('waxStampMark');
            stampMark.classList.remove('hidden');

            state.resonance = Math.min(100, state.resonance + 20);
            updateResonanceHUD();

            state.historyLog.push({
                speaker: 'Thủ Tục Lịch Sử',
                role: 'Sổ Thuyền Viên Chargeurs Réunis 1911',
                text: `Xác nhận ghi danh: ${pName} (${pAge} tuổi) — Chức vụ: Aide-cuisinier (Phụ Bếp) cùng thuyền viên Văn Ba (Nguyễn Tất Thành).`
            });
            updateLogModalContent();

            setTimeout(() => {
                document.getElementById('crewRegisterModal').classList.add('hidden');
                stampMark.classList.add('hidden');
                state.currentStepIndex = 6; // dock_3 gangway
                renderCurrentStep();
            }, 1800);
        }

        /* ----------------------------------------------------
         * 8. CẦN GẠT CÒI TÀU HƠI NƯỚC (TƯƠNG TÁC 4)
         * ---------------------------------------------------- */
        const leverHandle = document.getElementById('leverHandle');
        let isDraggingLever = false;
        let startDragY = 0;
        let currentPull = 0;
        const maxPull = 90;

        if (leverHandle) {
            leverHandle.addEventListener('mousedown', (e) => {
                isDraggingLever = true;
                startDragY = e.clientY;
                document.body.style.cursor = 'ns-resize';
            });
        }

        window.addEventListener('mousemove', (e) => {
            if (!isDraggingLever || !leverHandle) return;
            const delta = Math.max(0, Math.min(maxPull, e.clientY - startDragY));
            currentPull = delta;
            leverHandle.style.transform = `translateY(${delta}px)`;
            if (currentPull > 30) emitSteamBurst();
        });

        window.addEventListener('mouseup', () => {
            if (!isDraggingLever || !leverHandle) return;
            isDraggingLever = false;
            document.body.style.cursor = '';

            if (currentPull > 25) {
                const intensity = Math.min(0.4, (currentPull / maxPull) * 0.35);
                playShipHorn(intensity);
                state.resonance = Math.min(100, state.resonance + 10);
                updateResonanceHUD();

                setTimeout(() => {
                    document.getElementById('whistleLeverStation').classList.add('hidden');
                    state.currentStepIndex = 7; // ship_1 boiler
                    renderCurrentStep();
                }, 1500);
            }

            leverHandle.style.transition = 'transform 0.25s var(--ease-snap)';
            leverHandle.style.transform = 'translateY(0px)';
            playLeverSpringSound();
            setTimeout(() => {
                leverHandle.style.transition = '';
                currentPull = 0;
            }, 250);
        });

        /* ----------------------------------------------------
         * 9. XÚC THAN HẦM LÒ 40°C (TƯƠNG TÁC 5)
         * ---------------------------------------------------- */
        const shovel = document.getElementById('draggableShovel');
        if (shovel) {
            shovel.addEventListener('click', () => {
                playFurnaceSound();
                emitSparks(window.innerWidth / 2, window.innerHeight / 2, 0);
                state.resonance = Math.min(100, state.resonance + 15);
                updateResonanceHUD();
                setTimeout(finishCoalShovel, 1200);
            });
        }

        function finishCoalShovel() {
            document.getElementById('coalShovelModal').classList.add('hidden');
            state.currentStepIndex = 8; // ship_1_dialogue
            renderCurrentStep();
        }

        /* ----------------------------------------------------
         * 10. SỔ TAY TỪ VỰNG TIẾNG PHÁP (TƯƠNG TÁC 6)
         * ---------------------------------------------------- */
        function flipNotebookPage() {
            playPageTurnSound();
            if (state.notebookPage === 1) {
                state.notebookPage = 2;
                document.getElementById('notebookPageNum').textContent = 'Trang 2 / 2';
                document.getElementById('notebookContent').innerHTML = `
                    <div class="p-2 rounded bg-[#ece1c5] border-l-4 border-amber-700">
                        <strong class="text-amber-950 font-bold">le peuple</strong> : Nhân dân, Quần chúng
                    </div>
                    <div class="p-2 rounded bg-[#ece1c5] border-l-4 border-amber-700">
                        <strong class="text-amber-950 font-bold">le travail</strong> : Lao động, Việc làm
                    </div>
                    <div class="p-2 rounded bg-[#ece1c5] border-l-4 border-amber-700">
                        <strong class="text-amber-950 font-bold">l'indépendance</strong> : Độc lập, Tự chủ
                    </div>
                    <div class="p-2 rounded bg-[#f3ecd8] border border-[#8c6d48]/40 text-[11px] text-[#5c3e23] italic">
                        "Ghi chú: Mỗi ngày học mười từ, viết lên cánh tay và mẩu giấy vụn khi làm bếp..."
                    </div>
                `;
                document.getElementById('btnFlipNotebook').innerHTML = `
                    <span>Đã Học Xong & Tiếp Tục</span>
                    <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
                `;
            } else {
                document.getElementById('frenchNotebookModal').classList.add('hidden');
                state.notebookPage = 1;
                state.currentStepIndex = 10; // ship_2_dialogue
                renderCurrentStep();
            }
        }

        /* ----------------------------------------------------
         * 11. LUẬN CƯƠNG LÊNIN & ĐƯỜNG KÁCH MỆNH & PÁC BÓ
         * ---------------------------------------------------- */
        function finishThesisMagnifier() {
            playPledgeChime();
            state.resonance = Math.min(100, state.resonance + 15);
            updateResonanceHUD();
            document.getElementById('thesisMagnifierModal').classList.add('hidden');
            state.currentStepIndex = 12; // act4_1_quote
            renderCurrentStep();
        }

        function finishDuongKachMenh() {
            playPageTurnSound();
            state.resonance = Math.min(100, state.resonance + 10);
            updateResonanceHUD();
            document.getElementById('duongKachMenhModal').classList.add('hidden');
            state.currentStepIndex = 14; // act4_3 party founded
            renderCurrentStep();
        }

        function touchMilestoneSuccess() {
            playStoneChime();
            document.getElementById('milestoneTarget').classList.add('ring-4', 'ring-amber-400', 'scale-110');
            document.getElementById('cheLanVienPoem').classList.remove('hidden');
            state.resonance = 100;
            updateResonanceHUD();
        }

        function finishMilestone() {
            document.getElementById('milestone108Modal').classList.add('hidden');
            state.currentStepIndex = 16; // act5_2 Pac Bo lamp
            renderCurrentStep();
        }

        /* ----------------------------------------------------
         * 12. RENDER CURRENT STEP (STAGE DUAL CROSS-FADING ENGINE)
         * ---------------------------------------------------- */
        function renderCurrentStep() {
            const step = SCENE_SCRIPT[state.currentStepIndex];
            if (!step) return;

            // 1. HUD Updates
            document.getElementById('hudActBadge').textContent = step.act;
            document.getElementById('hudLocationTitle').textContent = step.location;
            document.getElementById('hudCoordinates').textContent = step.coords;
            document.getElementById('stepActSummary').textContent = `Hồi ${step.actIndex}/5:`;
            document.getElementById('stepSceneTitle').textContent = step.sceneNum;
            document.getElementById('stepIndicator').textContent = `${state.currentStepIndex + 1} / ${SCENE_SCRIPT.length}`;

            // 2. Speaker Badge Colors
            const badge = document.getElementById('speakerBadge');
            badge.textContent = step.speaker;
            document.getElementById('speakerRole').textContent = step.role;

            if (step.speaker === 'Văn Ba' || step.speaker === 'Nguyễn Tất Thành') {
                badge.className = 'px-3 py-1 rounded bg-amber-500/20 border border-amber-400/50 text-amber-300 font-cinematic text-xs md:text-sm font-bold tracking-widest uppercase shadow-[0_0_15px_rgba(245,158,11,0.25)]';
            } else if (step.speaker === 'Nguyễn Ái Quốc') {
                badge.className = 'px-3 py-1 rounded bg-red-900/40 border border-red-500/60 text-red-200 font-cinematic text-xs md:text-sm font-bold tracking-widest uppercase shadow-[0_0_15px_rgba(220,38,38,0.3)]';
            } else {
                badge.className = 'px-3 py-1 rounded bg-slate-800 border border-slate-700 text-slate-300 font-cinematic text-xs md:text-sm font-bold tracking-widest uppercase';
            }

            // 3. Smooth 60 FPS Dual Cross-Dissolve Stage Background
            const bgA = document.getElementById('bgLayerA');
            const bgB = document.getElementById('bgLayerB');

            if (state.activeBgLayer === 'A') {
                bgB.src = step.image;
                bgB.className = `absolute inset-0 w-full h-full object-cover object-center transition-opacity duration-1000 filter brightness-[0.92] contrast-105 kenburns-${(state.currentStepIndex % 3) + 1} opacity-100`;
                bgA.className = 'absolute inset-0 w-full h-full object-cover object-center transition-opacity duration-1000 filter brightness-[0.92] contrast-105 opacity-0';
                state.activeBgLayer = 'B';
            } else {
                bgA.src = step.image;
                bgA.className = `absolute inset-0 w-full h-full object-cover object-center transition-opacity duration-1000 filter brightness-[0.92] contrast-105 kenburns-${(state.currentStepIndex % 3) + 1} opacity-100`;
                bgB.className = 'absolute inset-0 w-full h-full object-cover object-center transition-opacity duration-1000 filter brightness-[0.92] contrast-105 opacity-0';
                state.activeBgLayer = 'A';
            }

            // 4. History Logging
            state.historyLog.push({ speaker: step.speaker, role: step.role, text: step.text });
            updateLogModalContent();

            // 5. Check Choices
            const choicesContainer = document.getElementById('choicesContainer');
            const dialogueBox = document.getElementById('dialogueBox');

            if (step.isChoice) {
                state.waitingForChoice = true;
                choicesContainer.classList.remove('hidden');
                dialogueBox.classList.add('opacity-90');
                renderChoices(step.choices);
            } else {
                state.waitingForChoice = false;
                choicesContainer.classList.add('hidden');
                dialogueBox.classList.remove('opacity-90');
            }

            // 6. Action Triggers
            handleActionTriggers(step.action);

            // 7. Start Kinetic Typewriter
            startTypewriter(step.text);
        }

        function handleActionTriggers(action) {
            // Hide all widgets by default unless triggered
            const pledgeDrag = document.getElementById('pledgeDragContainer');
            const crewReg = document.getElementById('crewRegisterModal');
            const whistleLever = document.getElementById('whistleLeverStation');
            const coalModal = document.getElementById('coalShovelModal');
            const notebookModal = document.getElementById('frenchNotebookModal');
            const thesisModal = document.getElementById('thesisMagnifierModal');
            const duongKachMenh = document.getElementById('duongKachMenhModal');
            const milestoneModal = document.getElementById('milestone108Modal');
            const dawnModal = document.getElementById('dawnBloomModal');

            if (action === 'pledge_drag_trigger') {
                state.isPledgePending = true;
                pledgeDrag.classList.remove('hidden');
            } else {
                state.isPledgePending = false;
                pledgeDrag.classList.add('hidden');
            }

            if (action === 'crew_register_trigger') crewReg.classList.remove('hidden');
            if (action === 'whistle_trigger') whistleLever.classList.remove('hidden');
            if (action === 'coal_shovel_trigger') coalModal.classList.remove('hidden');
            if (action === 'notebook_trigger') notebookModal.classList.remove('hidden');
            if (action === 'thesis_magnifier_trigger') thesisModal.classList.remove('hidden');
            if (action === 'duongkachmenh_trigger') duongKachMenh.classList.remove('hidden');
            if (action === 'milestone_trigger') milestoneModal.classList.remove('hidden');
            if (action === 'dawn_bloom_trigger') {
                playDawnBloomChord();
                dawnModal.classList.remove('hidden');
            }
        }

        function startTypewriter(text) {
            clearInterval(state.typingTimer);
            state.isTyping = true;
            state.fullText = text;
            const target = document.getElementById('dialogueContent');
            target.innerHTML = '';

            let charIdx = 0;
            const speed = 25;

            state.typingTimer = setInterval(() => {
                if (charIdx < text.length) {
                    target.textContent += text[charIdx];
                    if (charIdx % 2 === 0) playTypewriterKey();
                    charIdx++;
                } else {
                    finishTypewriter();
                }
            }, speed);
        }

        function finishTypewriter() {
            clearInterval(state.typingTimer);
            state.isTyping = false;
            document.getElementById('dialogueContent').textContent = state.fullText;

            if (state.autoPlay && !state.waitingForChoice && !state.isPledgePending) {
                clearTimeout(state.autoPlayTimer);
                state.autoPlayTimer = setTimeout(advanceDialogue, 4000);
            }
        }

        function advanceDialogue() {
            if (state.waitingForChoice || state.isPledgePending) return;

            if (state.isTyping) {
                finishTypewriter();
                return;
            }

            if (state.currentStepIndex < SCENE_SCRIPT.length - 1) {
                state.currentStepIndex++;
                renderCurrentStep();
            } else {
                // Finale reached
                document.getElementById('dawnBloomModal').classList.remove('hidden');
            }
        }

        function renderChoices(choices) {
            const list = document.getElementById('choicesList');
            list.innerHTML = '';

            choices.forEach((c) => {
                const btn = document.createElement('button');
                btn.className = 'p-3.5 rounded-xl border border-brass/40 bg-abyss/90 hover:bg-brass/25 hover:border-brass text-left text-xs md:text-sm text-slate-100 transition-all flex items-start gap-2.5 cursor-pointer focus-visible:ring-2 focus-visible:ring-brass group';
                btn.onclick = (e) => {
                    e.stopPropagation();
                    selectChoice(c);
                };

                btn.innerHTML = `
                    <span class="inline-flex items-center justify-center min-w-[24px] h-6 rounded bg-brass/20 text-brass font-typewriter font-bold text-xs group-hover:bg-brass group-hover:text-void transition-colors">
                        [${c.key}]
                    </span>
                    <span class="leading-snug">${c.label}</span>
                `;
                list.appendChild(btn);
            });
        }

        function selectChoice(choice) {
            state.waitingForChoice = false;
            document.getElementById('choicesContainer').classList.add('hidden');

            state.resonance = Math.min(100, state.resonance + choice.resonanceGain);
            updateResonanceHUD();

            const targetIdx = SCENE_SCRIPT.findIndex(s => s.id === choice.nextId);
            if (targetIdx !== -1) state.currentStepIndex = targetIdx;
            else state.currentStepIndex++;

            renderCurrentStep();
        }

        function handleDialogueBoxClick() {
            advanceDialogue();
        }

        function updateResonanceHUD() {
            document.getElementById('resonanceScore').textContent = `${state.resonance}%`;
            document.getElementById('resonanceBar').style.width = `${state.resonance}%`;
        }

        /* ----------------------------------------------------
         * 13. TIME LENS & CHAPTER JUMPS & AUDIO
         * ---------------------------------------------------- */
        function toggleTimeLens() {
            state.timeLensActive = !state.timeLensActive;
            const container = document.getElementById('timeLensContainer');
            const btn = document.getElementById('btnTimeLens');

            if (state.timeLensActive) {
                container.classList.remove('hidden');
                btn.classList.add('bg-cyan-500', 'text-slate-950', 'shadow-[0_0_25px_rgba(6,182,212,0.8)]');
                btn.classList.remove('bg-cyan-950/40', 'text-cyan-300');
                playTypewriterKey();
            } else {
                container.classList.add('hidden');
                btn.classList.remove('bg-cyan-500', 'text-slate-950', 'shadow-[0_0_25px_rgba(6,182,212,0.8)]');
                btn.classList.add('bg-cyan-950/40', 'text-cyan-300');
            }
        }

        window.addEventListener('mousemove', (e) => {
            if (state.timeLensActive) {
                const lens = document.getElementById('lensCursor');
                lens.style.left = `${e.clientX}px`;
                lens.style.top = `${e.clientY}px`;
            }
        });

        function toggleChapterMenu(open) {
            const modal = document.getElementById('chapterMenuModal');
            if (open) modal.classList.remove('hidden');
            else modal.classList.add('hidden');
        }

        function jumpToChapter(target) {
            toggleChapterMenu(false);
            if (target === 'prologue') {
                openPrologue();
            } else {
                state.prologueActive = false;
                document.getElementById('prologueStage').classList.add('hidden');
                state.currentStepIndex = target;
                renderCurrentStep();
            }
        }

        function openPrologue() {
            state.prologueActive = true;
            state.prologueIndex = 0;
            const pStage = document.getElementById('prologueStage');
            pStage.classList.remove('hidden', 'opacity-0', 'pointer-events-none');
            startPrologueSoundtrack();
            renderPrologueSlide();
        }

        function toggleLogModal(open) {
            const modal = document.getElementById('logModal');
            if (open) modal.classList.remove('hidden');
            else modal.classList.add('hidden');
        }

        function updateLogModalContent() {
            const container = document.getElementById('logContainer');
            if (!container) return;
            container.innerHTML = state.historyLog.map(item => `
                <div class="p-3 rounded-lg bg-void/70 border border-slate-800">
                    <div class="flex items-center justify-between text-xs text-brass font-cinematic font-bold mb-1">
                        <span>${item.speaker}</span>
                        <span class="text-[10px] text-slate-500 font-typewriter font-normal">${item.role}</span>
                    </div>
                    <p class="text-slate-200 text-xs md:text-sm leading-relaxed">${item.text}</p>
                </div>
            `).join('');
            container.scrollTop = container.scrollHeight;
        }

        function toggleAudio() {
            initAudioContext();
            state.audioEnabled = !state.audioEnabled;
            const iconOn = document.getElementById('iconAudioOn');
            const iconOff = document.getElementById('iconAudioOff');
            const audioEl = document.getElementById('prologueBgmAudio');

            if (audioEl) audioEl.muted = !state.audioEnabled;

            if (state.audioEnabled) {
                iconOn.classList.remove('hidden');
                iconOff.classList.add('hidden');
                if (state.prologueActive && (!audioEl || audioEl.paused)) startPrologueSoundtrack();
            } else {
                iconOn.classList.add('hidden');
                iconOff.classList.remove('hidden');
                if (prologueMusicState.pureSineGain && audioCtx) prologueMusicState.pureSineGain.gain.setValueAtTime(0.0001, audioCtx.currentTime);
            }
        }

        function toggleAutoPlay() {
            state.autoPlay = !state.autoPlay;
            const btn = document.getElementById('btnAutoPlay');
            if (state.autoPlay) {
                btn.classList.add('bg-brass', 'text-void');
                btn.classList.remove('bg-abyss/80', 'text-brass');
                if (!state.isTyping && !state.waitingForChoice && !state.isPledgePending) advanceDialogue();
            } else {
                btn.classList.remove('bg-brass', 'text-void');
                btn.classList.add('bg-abyss/80', 'text-brass');
                clearTimeout(state.autoPlayTimer);
            }
        }

        function restartExperience() {
            document.getElementById('dawnBloomModal').classList.add('hidden');
            state.resonance = 25;
            updateResonanceHUD();
            openPrologue();
        }

        // Global Keyboard Shortcut Listeners
        window.addEventListener('keydown', (e) => {
            if (state.prologueActive) {
                startPrologueSoundtrack();
                if (e.code === 'Space' || e.code === 'Enter' || e.key === 'ArrowRight') {
                    e.preventDefault();
                    nextPrologueSlide();
                } else if (e.key === 'ArrowLeft') {
                    e.preventDefault();
                    prevPrologueSlide();
                } else if (e.code === 'Escape') {
                    e.preventDefault();
                    skipPrologue();
                }
                return;
            }

            if (e.code === 'Space' || e.code === 'Enter') {
                e.preventDefault();
                advanceDialogue();
            } else if (e.key === '1' && state.waitingForChoice) {
                const step = SCENE_SCRIPT[state.currentStepIndex];
                if (step && step.choices && step.choices[0]) selectChoice(step.choices[0]);
            } else if (e.key === '2' && state.waitingForChoice) {
                const step = SCENE_SCRIPT[state.currentStepIndex];
                if (step && step.choices && step.choices[1]) selectChoice(step.choices[1]);
            } else if (e.key.toLowerCase() === 't') {
                toggleTimeLens();
            } else if (e.key.toLowerCase() === 'm') {
                toggleAudio();
            } else if (e.key.toLowerCase() === 'c') {
                toggleChapterMenu(true);
            } else if (e.key.toLowerCase() === 'a') {
                toggleAutoPlay();
            } else if (e.key.toLowerCase() === 'l') {
                toggleLogModal(document.getElementById('logModal').classList.contains('hidden'));
            } else if (e.key.toLowerCase() === 'r') {
                restartExperience();
            } else if (e.code === 'Escape') {
                toggleLogModal(false);
                toggleChapterMenu(false);
            }
        });

        /* ----------------------------------------------------
         * 14. ATMOSPHERIC PARTICLES & SMOKE OVERLAYS (60 FPS)
         * ---------------------------------------------------- */
        const canvas = document.getElementById('skyCanvas');
        const ctx = canvas ? canvas.getContext('2d') : null;
        let stars = [];

        function resizeCanvas() {
            if (!canvas) return;
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            stars = [];
            for (let i = 0; i < 90; i++) {
                stars.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * (canvas.height * 0.7),
                    r: Math.random() * 1.5 + 0.4,
                    alpha: Math.random() * 0.8 + 0.2,
                    speed: Math.random() * 0.02 + 0.005
                });
            }
        }

        function drawSky() {
            if (!ctx) return;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let s of stars) {
                s.alpha += s.speed;
                if (s.alpha > 1 || s.alpha < 0.2) s.speed = -s.speed;
                ctx.fillStyle = `rgba(255, 235, 180, ${Math.abs(s.alpha)})`;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                ctx.fill();
            }
            requestAnimationFrame(drawSky);
        }

        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();
        requestAnimationFrame(drawSky);

        // Continuous Subtle Smoke / Harbor Steam
        const smokeCanvas = document.getElementById('smokeCanvas');
        const sCtx = smokeCanvas ? smokeCanvas.getContext('2d') : null;
        let smokeParticles = [];

        function resizeSmoke() {
            if (!smokeCanvas) return;
            smokeCanvas.width = window.innerWidth;
            smokeCanvas.height = window.innerHeight;
        }

        function emitSmoke() {
            if (smokeParticles.length < 25) {
                smokeParticles.push({
                    x: window.innerWidth * 0.6 + (Math.random() * 40 - 20),
                    y: window.innerHeight * 0.5,
                    vx: -(Math.random() * 0.6 + 0.3),
                    vy: -(Math.random() * 0.4 + 0.2),
                    radius: Math.random() * 16 + 10,
                    alpha: 0.25,
                    growth: Math.random() * 0.25 + 0.15,
                    isSteam: false
                });
            }
        }

        function emitSteamBurst() {
            for (let i = 0; i < 4; i++) {
                smokeParticles.push({
                    x: window.innerWidth * 0.62 + (Math.random() * 10 - 5),
                    y: window.innerHeight * 0.45,
                    vx: -(Math.random() * 1.6 + 1.0),
                    vy: -(Math.random() * 1.4 + 0.8),
                    radius: Math.random() * 12 + 8,
                    alpha: 0.7,
                    growth: Math.random() * 0.4 + 0.2,
                    isSteam: true
                });
            }
        }

        function drawSmoke() {
            if (!sCtx) return;
            sCtx.clearRect(0, 0, smokeCanvas.width, smokeCanvas.height);
            emitSmoke();

            for (let i = smokeParticles.length - 1; i >= 0; i--) {
                const p = smokeParticles[i];
                p.x += p.vx;
                p.y += p.vy;
                p.radius += p.growth;
                p.alpha -= p.isSteam ? 0.016 : 0.0035;

                if (p.alpha <= 0) {
                    smokeParticles.splice(i, 1);
                    continue;
                }

                const grad = sCtx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius);
                if (p.isSteam) {
                    grad.addColorStop(0, `rgba(240, 245, 255, ${p.alpha * 0.9})`);
                    grad.addColorStop(1, `rgba(200, 220, 255, 0)`);
                } else {
                    grad.addColorStop(0, `rgba(45, 55, 72, ${p.alpha * 0.5})`);
                    grad.addColorStop(1, `rgba(15, 23, 42, 0)`);
                }

                sCtx.fillStyle = grad;
                sCtx.beginPath();
                sCtx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                sCtx.fill();
            }

            requestAnimationFrame(drawSmoke);
        }

        window.addEventListener('resize', () => {
            resizeSmoke();
            resizePrologueVfx();
        });
        resizeSmoke();
        resizePrologueVfx();
        requestAnimationFrame(drawSmoke);

        // Ambient Lamp Flicker
        const flickerCanvas = document.getElementById('ambientFlickerCanvas');
        const fCtx = flickerCanvas ? flickerCanvas.getContext('2d') : null;
        let flickerTime = 0;

        function resizeFlicker() {
            if (!flickerCanvas) return;
            flickerCanvas.width = window.innerWidth;
            flickerCanvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeFlicker);
        resizeFlicker();

        function drawFlicker() {
            if (!fCtx) return;
            flickerTime += 0.04;
            fCtx.clearRect(0, 0, flickerCanvas.width, flickerCanvas.height);

            // Subtle warm amber ambient glow in the room/table
            const intensity = 0.035 + Math.sin(flickerTime * 2.3) * 0.008 + Math.cos(flickerTime * 4.7) * 0.005;
            const grad = fCtx.createRadialGradient(
                flickerCanvas.width * 0.35, flickerCanvas.height * 0.65, 10,
                flickerCanvas.width * 0.35, flickerCanvas.height * 0.65, flickerCanvas.width * 0.5
            );
            grad.addColorStop(0, `rgba(245, 158, 11, ${intensity * 1.8})`);
            grad.addColorStop(1, 'rgba(245, 158, 11, 0)');

            fCtx.fillStyle = grad;
            fCtx.fillRect(0, 0, flickerCanvas.width, flickerCanvas.height);
            requestAnimationFrame(drawFlicker);
        }
        requestAnimationFrame(drawFlicker);

        // Initialize Prologue on startup
        renderPrologueSlide();
    </script>
</body>
</html>
'''

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"preview.html successfully generated! Size: {len(HTML_CONTENT)} characters.")
