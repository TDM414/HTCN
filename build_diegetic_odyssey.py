# -*- coding: utf-8 -*-
"""
Builder for the 100% Diegetic In-Scene Experience:
"Hải Trình 1911 – 1941: Thiên Sử Thi Của Ngọn Lửa"
6 Hồi lịch sử • 24 Phân cảnh chi tiết • 0 Pop-up • 100% In-Scene Interactions
"""

import os

HTML_CODE = r'''<!DOCTYPE html>
<html lang="vi" class="h-full bg-slate-950 text-slate-100 antialiased select-none">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Hải Trình 1911 – 1941: Thiên Sử Thi Của Ngọn Lửa • Tư Tưởng Hồ Chí Minh</title>
    
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

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600&display=swap" rel="stylesheet">

    <!-- Preload Cinematic Assets -->
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
    <link rel="preload" as="image" href="marseille_disembark.jpg">
    <link rel="preload" as="image" href="marseille_deck_lookout.jpg">
    <link rel="preload" as="image" href="marseille_1_port.jpg">
    <link rel="preload" as="image" href="marseille_left_carts.jpg">
    <link rel="preload" as="image" href="marseille_right_steps.jpg">
    <link rel="preload" as="image" href="world_1_boston_london.jpg">
    <link rel="preload" as="image" href="act4_1_versailles_1919.jpg">
    <link rel="preload" as="image" href="act4_2_paris_room.jpg">
    <link rel="preload" as="image" href="act4_3_tours_congress.jpg">
    <link rel="preload" as="image" href="act5_1_moscow_1923.jpg">
    <link rel="preload" as="image" href="act5_2_guangzhou_school.jpg">
    <link rel="preload" as="image" href="act5_3_hongkong_unification.jpg">
    <link rel="preload" as="image" href="act5_1_pacbo_return.jpg">
    <link rel="preload" as="image" href="act5_2_pacbo_lamp.jpg">
    <link rel="preload" as="image" href="act5_3_sunrise_independence.jpg">

    <style>
        :root {
            --color-void: #03050a;
            --color-abyss: #070c18;
            --color-brass: #d4a348;
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

        /* Ken Burns animations */
        @keyframes kbSlide1 { 0% { transform: scale(1.0) translate(0, 0); } 100% { transform: scale(1.07) translate(-1.5%, 1.0%); } }
        @keyframes kbSlide2 { 0% { transform: scale(1.07) translate(1.2%, 1.0%); } 100% { transform: scale(1.01) translate(-1%, -0.8%); } }
        @keyframes kbSlide3 { 0% { transform: scale(1.02) translate(-1.2%, 0.5%); } 100% { transform: scale(1.06) translate(1.4%, -0.8%); } }

        .kenburns-1 { animation: kbSlide1 22s cubic-bezier(0.25, 1, 0.5, 1) forwards !important; }
        .kenburns-2 { animation: kbSlide2 22s cubic-bezier(0.25, 1, 0.5, 1) forwards !important; }
        .kenburns-3 { animation: kbSlide3 22s cubic-bezier(0.25, 1, 0.5, 1) forwards !important; }

        /* Floating subtitles animation */
        @keyframes cinemaTextIn {
            0% { opacity: 0; transform: translateY(20px); filter: blur(6px); }
            100% { opacity: 1; transform: translateY(0); filter: blur(0px); }
        }
        .cinema-title-animate { animation: cinemaTextIn 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
        .cinema-subtext-animate { animation: cinemaTextIn 0.95s cubic-bezier(0.16, 1, 0.3, 1) 0.15s both; }

        /* Dialogue Card */
        .dialogue-card {
            background: rgba(7, 12, 24, 0.93);
            border: 1px solid rgba(212, 163, 72, 0.42);
            box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.95), 0 0 35px rgba(212, 163, 72, 0.16);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
        }

        /* Diegetic interactive prop styling */
        .diegetic-prop {
            filter: drop-shadow(0 15px 25px rgba(0,0,0,0.9));
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), filter 0.2s ease;
        }
        .diegetic-prop:hover {
            filter: drop-shadow(0 20px 35px rgba(245, 158, 11, 0.4)) brightness(1.1);
        }
        .hud-element {
            transition: opacity 0.3s ease, transform 0.3s ease;
        }
        @keyframes rumble {
            0%, 100% { transform: translate(0, 0); }
            20% { transform: translate(-3px, 2px); }
            40% { transform: translate(3px, -2px); }
            60% { transform: translate(-2px, -2px); }
            80% { transform: translate(2px, 2px); }
        }
        .animate-rumble {
            animation: rumble 0.25s ease-in-out 2;
        }

        /* Striker strip texture */
        .striker-strip {
            background: repeating-linear-gradient(45deg, #2e1b10, #2e1b10 2px, #452817 2px, #452817 4px);
            box-shadow: inset 0 0 4px rgba(0,0,0,0.8);
        }

        /* Furnace fire aura */
        @keyframes fireGlow {
            0%, 100% { opacity: 0.85; filter: drop-shadow(0 0 35px rgba(234, 88, 12, 0.8)); }
            50% { opacity: 1; filter: drop-shadow(0 0 65px rgba(245, 158, 11, 1)); }
        }
        .animate-fire { animation: fireGlow 2.5s ease-in-out infinite; }

        /* Marseille camera whip-pan & motion blur transitions */
        @keyframes whipLeft {
            0% { transform: scale(1) translateX(0); filter: blur(0px); }
            40% { transform: scale(1.05) translateX(35px); filter: blur(14px); }
            100% { transform: scale(1) translateX(0); filter: blur(0px); }
        }
        @keyframes whipRight {
            0% { transform: scale(1) translateX(0); filter: blur(0px); }
            40% { transform: scale(1.05) translateX(-35px); filter: blur(14px); }
            100% { transform: scale(1) translateX(0); filter: blur(0px); }
        }
        @keyframes whipCenter {
            0% { transform: scale(1) translateY(0); filter: blur(0px); }
            40% { transform: scale(1.04) translateY(-20px); filter: blur(12px); }
            100% { transform: scale(1) translateY(0); filter: blur(0px); }
        }
        .marseille-whip-left { animation: whipLeft 0.55s cubic-bezier(0.16, 1, 0.3, 1) forwards !important; }
        .marseille-whip-right { animation: whipRight 0.55s cubic-bezier(0.16, 1, 0.3, 1) forwards !important; }
        .marseille-whip-center { animation: whipCenter 0.55s cubic-bezier(0.16, 1, 0.3, 1) forwards !important; }
    </style>
</head>
<body class="flex items-center justify-center bg-black overflow-hidden">

    <!-- 16:9 Theatrical Stage -->
    <div id="stageContainer" class="stage-viewport relative overflow-hidden bg-void flex flex-col justify-between shadow-2xl">
        
        <!-- ========================================== -->
        <!-- CINEMATIC BACKGROUND CANVAS (CROSS-FADING) -->
        <!-- ========================================== -->
        <div id="mainBgStage" class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
            <img id="bgLayerA" src="inn_1_talking.jpg" alt="Minh họa lịch sử" 
                 class="absolute inset-0 w-full h-full object-cover object-center transition-opacity duration-1000 filter brightness-[0.92] contrast-105 kenburns-1 opacity-100">
            <img id="bgLayerB" src="inn_2_hands.jpg" alt="Minh họa lịch sử dự phòng" 
                 class="absolute inset-0 w-full h-full object-cover object-center transition-opacity duration-1000 filter brightness-[0.92] contrast-105 kenburns-2 opacity-0">
            
            <!-- Atmospheric VFX Overlays -->
            <canvas id="skyCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[1]"></canvas>
            <canvas id="smokeCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[2]"></canvas>
            <canvas id="sparkCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[3]"></canvas>
            <canvas id="ambientFlickerCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[4]"></canvas>
            
            <!-- Vignette & Horizon Lighting -->
            <div class="absolute inset-0 pointer-events-none z-[5]" style="background: radial-gradient(circle at 50% 50%, transparent 45%, rgba(3,5,10,0.85) 100%);"></div>
            <div class="absolute inset-x-0 bottom-0 h-64 bg-gradient-to-t from-black via-black/70 to-transparent pointer-events-none z-[5]"></div>
            <div class="absolute inset-x-0 top-0 h-28 bg-gradient-to-b from-black/80 to-transparent pointer-events-none z-[5]"></div>
        </div>

        <!-- ========================================== -->
        <!-- HUD HEADER -->
        <!-- ========================================== -->
        <header class="hud-element relative z-20 flex items-center justify-between px-6 py-4 bg-gradient-to-b from-void/95 via-void/60 to-transparent pointer-events-auto">
            <div class="flex items-center gap-4">
                <button onclick="toggleChapterMenu(true)" title="Danh Mục 6 Hồi Ký (Phím C)" aria-label="Menu Hồi Ký"
                        class="w-11 h-11 rounded-full border border-brass/50 bg-abyss/90 flex items-center justify-center text-brass hover:bg-brass/20 transition-all cursor-pointer shadow-[0_0_15px_rgba(212,163,72,0.25)] focus-visible:ring-2 focus-visible:ring-brass">
                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                </button>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
                        <span id="hudActBadge" class="text-xs font-semibold tracking-widest uppercase text-brass font-cinematic">HỒI 1 • LỜI THỀ GÁC TRỌ</span>
                    </div>
                    <h1 id="hudLocationTitle" class="text-sm md:text-base font-bold text-slate-100 tracking-wide">Căn Gác Trọ Nhỏ — Sài Gòn</h1>
                    <p id="hudCoordinates" class="text-[11px] text-slate-400 font-typewriter tracking-tight">10°46'N 106°42'E • Đầu Tháng 06/1911 (Đêm)</p>
                </div>
            </div>

            <!-- Resonance Indicator -->
            <div class="hidden md:flex items-center gap-3 px-4 py-2 rounded-full border border-brass/35 bg-abyss/80 backdrop-blur-md shadow-lg">
                <svg class="w-4 h-4 text-amber-400" viewBox="0 0 24 24" fill="currentColor">
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

            <!-- Controls -->
            <div class="flex items-center gap-2">
                <!-- Thấu Kính Button -->
                <button id="btnTimeLens" onclick="toggleTimeLens()" title="Thấu Kính Xuyên Thời Gian (Phím T)"
                        class="min-w-[44px] min-h-[44px] px-3 py-2 rounded-xl border border-cyan-400/50 bg-cyan-950/40 hover:bg-cyan-900/60 text-cyan-300 font-cinematic text-xs font-bold tracking-wider flex items-center gap-2 cursor-pointer transition-all shadow-[0_0_15px_rgba(6,182,212,0.3)]">
                    <svg class="w-4 h-4 text-cyan-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="8"/><line x1="12" y1="2" x2="12" y2="4"/><line x1="12" y1="20" x2="12" y2="22"/><line x1="2" y1="12" x2="4" y2="12"/><line x1="20" y1="12" x2="22" y2="12"/></svg>
                    <span class="hidden sm:inline">Thấu Kính [T]</span>
                </button>

                <!-- Chapter Menu -->
                <button onclick="toggleChapterMenu(true)" title="Menu Hồi Ký (Phím C)"
                        class="min-w-[44px] min-h-[44px] px-3 py-2 rounded-xl border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass text-xs font-cinematic font-bold tracking-wider flex items-center gap-1.5 cursor-pointer">
                    <svg class="w-4 h-4 text-brass" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                    <span class="hidden md:inline">Hồi Ký [C]</span>
                </button>

                <!-- Audio Toggle -->
                <button id="btnAudioToggle" onclick="toggleAudio()" title="Âm thanh (Phím M)"
                        class="min-w-[44px] min-h-[44px] p-2.5 rounded-lg border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass transition-all flex items-center justify-center cursor-pointer">
                    <svg id="iconAudioOn" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    <svg id="iconAudioOff" class="w-5 h-5 hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                </button>

                <!-- Autoplay -->
                <button id="btnAutoPlay" onclick="toggleAutoPlay()" title="Tự động dẫn truyện (Phím A)"
                        class="min-w-[44px] min-h-[44px] p-2.5 rounded-lg border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass transition-all flex items-center justify-center cursor-pointer">
                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
                </button>

                <!-- History Log -->
                <button onclick="toggleLogModal(true)" title="Nhật ký hội thoại (Phím L)"
                        class="min-w-[44px] min-h-[44px] p-2.5 rounded-lg border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass transition-all flex items-center justify-center cursor-pointer">
                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                </button>

                <!-- Hide UI (Phím H - Chuẩn LoL Spirit Blossom) -->
                <button id="btnToggleUI" onclick="toggleHideUI()" title="Ẩn/Hiện toàn bộ giao diện [Phím H]"
                        class="min-w-[44px] min-h-[44px] px-2.5 py-2 rounded-lg border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass text-xs font-cinematic font-bold tracking-wider flex items-center gap-1.5 cursor-pointer">
                    <svg id="iconEyeOpen" class="w-4 h-4 text-brass" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                    <svg id="iconEyeClosed" class="w-4 h-4 text-amber-400 hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>
                    <span class="hidden xl:inline">Ẩn UI [H]</span>
                </button>
            </div>
        </header>

        <!-- ======================================================== -->
                <!-- ======================================================== -->
        <!-- POPUP CẬN CẢNH ĐỐT LÒ HƠI NƯỚC (CLOSE-UP WORKSHOP MODAL CHÂN THỰC 100%) -->
        <!-- ======================================================== -->
        <!-- ======================================================== -->
        <!-- POPUP CẬN CẢNH ĐỐT LÒ HƠI NƯỚC (CLOSE-UP WORKSHOP MODAL CHÂN THỰC 100%) -->
        <!-- ======================================================== -->
        <div id="boilerWorkshopModal" class="hidden absolute inset-0 z-50 bg-black/95 backdrop-blur-md flex items-center justify-center p-3 md:p-6 select-none animate-fade-in">
            <div class="relative w-full max-w-4xl bg-gradient-to-b from-[#1c1815] via-[#120f0d] to-[#0a0807] border-2 border-amber-600/70 rounded-2xl shadow-[0_25px_80px_rgba(0,0,0,1)] p-4 md:p-6 flex flex-col gap-4 overflow-hidden">
                
                <!-- Ambient ember particles / glow inside modal -->
                <div class="absolute -top-20 -right-20 w-80 h-80 rounded-full bg-orange-600/15 blur-3xl pointer-events-none"></div>
                <div class="absolute -bottom-20 -left-20 w-80 h-80 rounded-full bg-amber-600/10 blur-3xl pointer-events-none"></div>

                <!-- Modal Header -->
                <div class="relative z-10 flex items-center justify-between border-b border-amber-500/30 pb-3">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-400 flex items-center justify-center text-amber-400 text-lg shadow-md shrink-0">
                            🔥
                        </div>
                        <div>
                            <div class="flex items-center gap-2">
                                <span class="text-xs md:text-sm font-cinematic font-bold text-amber-300 uppercase tracking-widest">
                                    CẬN CẢNH: CỬA LÒ NỒI HƠI TÀU AMIRAL LATOUCHE-TRÉVILLE
                                </span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-red-950 text-red-300 border border-red-700/60 font-typewriter">
                                    42°C
                                </span>
                            </div>
                            <p id="modalInstructionText" class="text-xs text-amber-100 font-typewriter mt-0.5">
                                Kéo từng cục than đá antraxit bên dưới (hoặc bấm chọn) ném vào ngọn lửa rực hồng để giữ áp suất cho con tàu!
                            </p>
                        </div>
                    </div>

                    <div class="flex items-center gap-3">
                        <!-- Progress counter -->
                        <div class="text-right pl-3 border-l border-amber-500/30 shrink-0">
                            <span class="text-[9px] text-slate-400 font-typewriter uppercase block">Tiến độ nạp than</span>
                            <span id="modalStokeCounter" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 font-typewriter font-bold text-xs border border-amber-500/40">
                                0 / 3 Cục Than
                            </span>
                        </div>
                        <!-- Close button -->
                        <button onclick="closeBoilerModal()" class="p-2 text-slate-400 hover:text-white hover:bg-white/10 rounded-lg transition cursor-pointer" title="Đóng cửa sổ">
                            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                        </button>
                    </div>
                </div>

                <!-- Modal Center Stage: Steam Gauge + Single Unified Boiler View -->
                <div class="relative z-10 flex flex-col gap-3">
                    
                    <!-- Top Steam Pressure Gauge Bar -->
                    <div class="w-full flex items-center justify-between px-4 py-2 rounded-xl bg-black/60 border border-amber-600/40 shadow-inner">
                        <div class="flex items-center gap-3">
                            <!-- Brass Dial -->
                            <div class="w-12 h-12 rounded-full bg-[#f4ecd8] border-2 border-amber-800 flex items-center justify-center relative shadow-md shrink-0">
                                <div id="modalGaugeNeedle" class="w-0.5 h-5 bg-red-700 origin-bottom transform -rotate-45 transition-transform duration-700 ease-out"></div>
                                <div class="absolute w-2 h-2 rounded-full bg-stone-900 border border-amber-600"></div>
                            </div>
                            <div>
                                <span class="text-[10px] text-slate-400 font-typewriter uppercase block">Đồng hồ áp suất hơi nước (Hãng Schneider)</span>
                                <span id="modalGaugeValue" class="text-xs md:text-sm font-cinematic font-bold text-amber-300 tracking-wider">
                                    Áp Suất: 35% (Mức Thấp)
                                </span>
                            </div>
                        </div>
                        <!-- Pressure bar visual -->
                        <div class="w-36 md:w-64 h-3 bg-stone-900 rounded-full border border-stone-700 overflow-hidden flex">
                            <div id="modalPressureBar" class="h-full bg-gradient-to-r from-amber-600 via-orange-500 to-red-500 transition-all duration-700" style="width: 35%;"></div>
                        </div>
                    </div>

                    <!-- Single Unified Boiler Furnace Stage (No split cards!) -->
                    <div id="modalFurnaceStage" class="relative rounded-2xl overflow-hidden border-2 border-stone-700 bg-black h-[320px] md:h-[380px] shadow-2xl flex flex-col justify-between p-3 select-none">
                        
                        <!-- Real Authentic Steamship Boiler Photo as Background -->
                        <img src="assets/boiler_furnace_authentic.jpg" alt="Mặt Lò Nồi Hơi Tàu Thủy 1911" 
                             class="absolute inset-0 w-full h-full object-cover filter contrast-115 brightness-95">
                        
                        <!-- Dark Vignette and Heat Overlays -->
                        <div class="absolute inset-0 bg-radial from-transparent via-black/25 to-black/80 pointer-events-none"></div>
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-black/40 pointer-events-none"></div>

                        <!-- Drop Target Area: The Roaring Firebox Door in Center -->
                        <div id="modalFurnaceTarget" 
                             class="absolute top-[8%] left-[10%] md:left-[15%] w-[80%] md:w-[70%] h-[58%] rounded-2xl border-2 border-dashed border-amber-400/80 bg-red-950/20 backdrop-blur-2xs flex flex-col items-center justify-center text-center shadow-[0_0_40px_rgba(245,158,11,0.4)] transition-all group pointer-events-auto">
                            <div class="px-3 py-1 rounded-full bg-black/85 border border-amber-400 shadow-xl flex items-center gap-1.5 animate-pulse">
                                <span class="text-xs">🔥</span>
                                <span class="text-[10px] md:text-xs font-cinematic font-bold text-amber-200 uppercase tracking-wider">
                                    CỬA LÒ RỰC LỬA — THẢ CỤC THAN VÀO ĐÂY
                                </span>
                            </div>
                            <span class="text-[9px] text-orange-200/90 font-typewriter mt-1">
                                (Nhiệt lượng > 1,200°C • Than Antraxit bốc cháy tức thì)
                            </span>
                        </div>

                        <!-- Bottom Authentic Coal Trough (Máng Than Đá Chân Thực) -->
                        <div class="relative z-20 mt-auto w-full max-w-2xl mx-auto rounded-xl bg-black/85 border border-amber-600/60 p-2.5 backdrop-blur-md shadow-2xl flex flex-col gap-1.5 pointer-events-auto">
                            <div class="flex items-center justify-between px-1">
                                <span class="text-[9px] md:text-[10px] text-amber-400 font-cinematic font-bold uppercase tracking-wider flex items-center gap-1">
                                    <span>🪨</span> MÁNG THAN TÀU THỦY (Chọn hoặc kéo từng cục than)
                                </span>
                                <span class="text-[9px] text-slate-400 font-typewriter">Than đá Wales 1911</span>
                            </div>

                            <!-- 3 Draggable Coal Chunks -->
                            <div class="flex items-center justify-around gap-2 pt-1">
                                
                                <div id="coalChunk1" 
                                     onpointerdown="startDragCoal(event, 1)"
                                     onclick="tossCoalChunk(1)"
                                     class="coal-chunk-item relative flex flex-col items-center cursor-grab active:cursor-grabbing hover:scale-110 active:scale-95 transition-all select-none touch-none group" 
                                     title="Kéo hoặc nhấp để ném cục than này vào lò">
                                    <div class="w-16 h-16 md:w-20 md:h-20 flex items-center justify-center">
                                        <img src="assets/coal_chunk_1.png" alt="Cục Than #1" 
                                             class="w-full h-full object-contain filter drop-shadow-[0_8px_16px_rgba(0,0,0,1)] group-hover:brightness-125 transition-all">
                                    </div>
                                    <span class="text-[9px] font-typewriter text-amber-300 font-bold px-2 py-0.5 rounded bg-black/90 border border-amber-600/50 mt-0.5 group-hover:border-amber-400">
                                        Cục Than #1
                                    </span>
                                </div>

                                <div id="coalChunk2" 
                                     onpointerdown="startDragCoal(event, 2)"
                                     onclick="tossCoalChunk(2)"
                                     class="coal-chunk-item relative flex flex-col items-center cursor-grab active:cursor-grabbing hover:scale-110 active:scale-95 transition-all select-none touch-none group" 
                                     title="Kéo hoặc nhấp để ném cục than này vào lò">
                                    <div class="w-16 h-16 md:w-20 md:h-20 flex items-center justify-center">
                                        <img src="assets/coal_chunk_2.png" alt="Cục Than #2" 
                                             class="w-full h-full object-contain filter drop-shadow-[0_8px_16px_rgba(0,0,0,1)] group-hover:brightness-125 transition-all">
                                    </div>
                                    <span class="text-[9px] font-typewriter text-amber-300 font-bold px-2 py-0.5 rounded bg-black/90 border border-amber-600/50 mt-0.5 group-hover:border-amber-400">
                                        Cục Than #2
                                    </span>
                                </div>

                                <div id="coalChunk3" 
                                     onpointerdown="startDragCoal(event, 3)"
                                     onclick="tossCoalChunk(3)"
                                     class="coal-chunk-item relative flex flex-col items-center cursor-grab active:cursor-grabbing hover:scale-110 active:scale-95 transition-all select-none touch-none group" 
                                     title="Kéo hoặc nhấp để ném cục than này vào lò">
                                    <div class="w-16 h-16 md:w-20 md:h-20 flex items-center justify-center">
                                        <img src="assets/coal_chunk_3.png" alt="Cục Than #3" 
                                             class="w-full h-full object-contain filter drop-shadow-[0_8px_16px_rgba(0,0,0,1)] group-hover:brightness-125 transition-all">
                                    </div>
                                    <span class="text-[9px] font-typewriter text-amber-300 font-bold px-2 py-0.5 rounded bg-black/90 border border-amber-600/50 mt-0.5 group-hover:border-amber-400">
                                        Cục Than #3
                                    </span>
                                </div>

                            </div>
                        </div>

                    </div>
                </div>

                <!-- Modal Footer Status -->
                <div class="relative z-10 flex items-center justify-between pt-2 border-t border-amber-500/20 text-xs font-typewriter text-slate-400">
                    <div class="flex items-center gap-2">
                        <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
                        <span id="modalFooterHint">Hướng dẫn: Kéo từng cục than thả vào cửa lò, hoặc nhấp thẳng vào cục than để ném vào ngọn lửa!</span>
                    </div>
                    <div class="text-amber-400 font-cinematic font-bold uppercase tracking-wider">
                        Tàu Amiral Latouche-Tréville
                    </div>
                </div>

            </div>
        </div>

        <!-- ======================================================== -->
        <!-- DIEGETIC IN-SCENE INTERACTIVE STAGE (100% IN-SCENE, NO POPUPS!) -->
        <!-- ======================================================== -->
        <div id="diegeticLayer" class="absolute inset-0 z-15 pointer-events-none">
            
            <!-- Hotspot nhấp nháy trên cửa lò than trong tranh nền -->
            <div id="furnaceHotspot" onclick="openBoilerModal()" 
                 class="hidden absolute top-[46%] right-[20%] z-20 flex flex-col items-center cursor-pointer group pointer-events-auto">
                <div class="relative flex items-center justify-center">
                    <div class="w-16 h-16 rounded-full bg-amber-500/25 animate-ping absolute"></div>
                    <div class="w-14 h-14 rounded-full bg-black/85 border-2 border-amber-400 flex items-center justify-center shadow-[0_0_25px_rgba(245,158,11,0.9)] group-hover:scale-110 group-hover:border-amber-300 transition-transform">
                        <svg class="w-7 h-7 text-amber-400 animate-pulse" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 2c-4 4.5-6 8-6 11.5 0 3.6 2.7 6.5 6 6.5s6-2.9 6-6.5c0-3.5-2-7-6-11.5zm0 15c-1.7 0-3-1.3-3-3 0-1.5 1-3 3-5 2 2 3 3.5 3 5 0 1.7-1.3 3-3 3z"/>
                        </svg>
                    </div>
                </div>
                <span class="mt-2 text-[11px] font-typewriter font-bold uppercase text-amber-300 bg-black/85 px-3 py-1 rounded-full border border-amber-500/60 shadow-lg group-hover:text-white group-hover:bg-amber-950/90 transition-all">
                    🔥 Nhấp vào đây để tiếp than
                </span>
            </div>

            <!-- 2. BẾN CẢNG 1911: SỔ THUYỀN VIÊN TRÊN MẶT BÀN GỖ BẾN TÀU -->
            <!-- ---------------------------------------------------- -->
            <div id="diegeticRegisterRig" class="hidden absolute inset-0 pointer-events-auto select-none flex items-center justify-center p-4">
                <div class="w-full max-w-xl bg-[#241a13] border-2 border-[#8c6d48] rounded-xl p-5 shadow-[0_25px_60px_rgba(0,0,0,0.95)] text-slate-200 relative">
                    <div class="text-center border-b border-[#8c6d48]/40 pb-2 mb-3">
                        <span class="text-[9px] uppercase font-typewriter text-amber-400 tracking-widest block">
                            COMPAGNIE DES CHARGEURS RÉUNIS • SAÏGON 05.06.1911
                        </span>
                        <h3 class="font-cinematic text-base md:text-lg font-bold text-amber-100 uppercase tracking-wider mt-0.5">
                            Sổ Thuyền Viên Tàu Amiral Latouche-Tréville
                        </h3>
                    </div>

                    <div class="space-y-2.5 font-typewriter text-xs">
                        <div class="p-2.5 rounded bg-[#2f2218] border border-[#8c6d48]/40 flex justify-between items-center">
                            <div>
                                <span class="text-[9px] text-amber-400 uppercase font-bold block">Thuyền viên 01:</span>
                                <span class="text-sm font-bold text-amber-100 font-cinematic">VĂN BA</span>
                                <span class="text-slate-400 text-[11px] ml-1">(21 tuổi)</span>
                            </div>
                            <span class="text-amber-300 font-semibold text-[11px]">Aide-cuisinier (Phụ Bếp) • 45 Francs/tháng</span>
                        </div>

                        <div class="p-2.5 rounded bg-[#382a1d] border-2 border-dashed border-amber-500/70 space-y-2">
                            <span class="text-[9px] text-amber-300 uppercase font-bold flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-ping"></span>
                                Thuyền viên 02 (Người bạn đồng hành tri kỷ):
                            </span>
                            <div class="grid grid-cols-2 gap-2">
                                <div>
                                    <label class="text-[9px] text-slate-400 uppercase block">Tên của bạn:</label>
                                    <input id="inscenePlayerName" type="text" value="Nguyễn Văn Đồng Hành" 
                                           onkeydown="event.stopPropagation()"
                                           class="w-full bg-[#1b140e] border border-[#8c6d48] rounded px-2.5 py-1 text-amber-200 font-typewriter text-xs focus:outline-none focus:border-amber-400">
                                </div>
                                <div>
                                    <label class="text-[9px] text-slate-400 uppercase block">Tuổi:</label>
                                    <input id="inscenePlayerAge" type="number" value="21" 
                                           onkeydown="event.stopPropagation()"
                                           class="w-full bg-[#1b140e] border border-[#8c6d48] rounded px-2.5 py-1 text-amber-200 font-typewriter text-xs focus:outline-none focus:border-amber-400">
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="mt-4 pt-3 border-t border-[#8c6d48]/40 flex items-center justify-between">
                        <span class="text-[11px] text-slate-400 font-typewriter">Chức vụ cố định: Aide-cuisinier</span>
                        <button onclick="stampInsceneRegister()" 
                                class="px-5 py-2 rounded-xl bg-gradient-to-r from-red-700 to-crimson hover:from-red-600 hover:to-red-700 text-white font-cinematic font-bold text-xs uppercase tracking-wider shadow-lg flex items-center gap-1.5 cursor-pointer active:scale-95 transition-transform">
                            <span>Đóng Dấu Mộc Son 1911</span>
                        </button>
                    </div>

                    <!-- Red Wax Stamp Mark on Paper -->
                    <div id="insceneStampMark" class="hidden absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-44 h-44 pointer-events-none transform -rotate-12 z-30">
                        <div class="w-full h-full rounded-full border-4 border-dashed border-red-600 bg-red-800/85 p-2 flex flex-col items-center justify-center text-center shadow-2xl backdrop-blur-xs animate-ping-once">
                            <span class="text-[9px] text-red-200 font-typewriter font-bold uppercase">CHARGEURS RÉUNIS</span>
                            <span class="text-xs font-cinematic text-white font-bold uppercase tracking-wider">ACCEPTÉ • 1911</span>
                            <span class="text-[8px] text-red-300 font-typewriter mt-0.5">SAÏGON - VAPEUR LATOUCHE</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ---------------------------------------------------- -->
            <!-- 2.5. HẢI TRÌNH 1911: HỌC TỪ MỚI DƯỚI ÁNH ĐÈN DẦU TRONG PHÒNG -->
            <!-- ---------------------------------------------------- -->
            <div id="diegeticStudyRig" class="hidden absolute inset-0 pointer-events-auto select-none flex flex-col items-center justify-center p-3 md:p-6 z-25">
                <div class="w-full max-w-4xl bg-[#1a120c]/95 border-2 border-[#8c6d48] rounded-2xl p-4 md:p-6 shadow-[0_25px_60px_rgba(0,0,0,0.95)] text-slate-200 relative backdrop-blur-md flex flex-col max-h-[90vh]">
                    
                    <!-- Rig Header -->
                    <div class="flex items-center justify-between border-b border-[#8c6d48]/40 pb-3 mb-3">
                        <div class="flex items-center gap-3">
                            <div class="w-9 h-9 rounded-full bg-amber-950/80 border border-amber-500/60 flex items-center justify-center shadow-[0_0_15px_rgba(245,158,11,0.5)]">
                                <span class="text-base animate-pulse">🪔</span>
                            </div>
                            <div>
                                <span class="text-[9px] uppercase font-typewriter text-amber-400 tracking-widest block font-bold">
                                    HẢI TRÌNH 1911 • ĐÊM ẤN ĐỘ DƯƠNG TRÊN TÀU LATOUCHE-TRÉVILLE
                                </span>
                                <h3 class="font-cinematic text-sm md:text-base font-bold text-amber-100 uppercase tracking-wider">
                                    Học Tiếng Pháp Cùng Anh Ba Dưới Ánh Đèn Dầu
                                </h3>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <span id="studyCounterBadge" class="px-3 py-1 rounded-full bg-black/70 border border-amber-500/50 text-amber-300 font-typewriter text-xs font-bold">
                                0 / 5 Từ Vựng
                            </span>
                        </div>
                    </div>

                    <!-- Main Interactive Study Area: Notebook & Vocabulary -->
                    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 flex-1 overflow-y-auto pr-1">
                        
                        <!-- Left: Open Vintage Parchment Notebook (col-span-7) -->
                        <div class="md:col-span-7 bg-[#231a12] border border-[#a07e56]/60 rounded-xl p-4 shadow-inner relative flex flex-col justify-between"
                             style="background-image: repeating-linear-gradient(transparent, transparent 27px, rgba(160, 126, 86, 0.15) 28px);">
                            
                            <!-- Notebook Header -->
                            <div class="flex items-center justify-between pb-2 border-b border-[#8c6d48]/30 mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="text-xs text-amber-400 font-serif italic">✏️ Cuốn Sổ Tay Thuyền Viên (1911)</span>
                                </div>
                                <span class="text-[10px] text-amber-300/70 font-typewriter">Mực tím & Bút chì</span>
                            </div>

                            <!-- List of Handwritten Entries -->
                            <div id="notebookWrittenWords" class="space-y-2.5 min-h-[160px] py-1">
                                <div id="notebookEmptyPrompt" class="text-center text-xs text-amber-200/50 italic py-8 font-serif">
                                    « Nhấp chọn từng từ vựng bên phải để cùng anh Ba nắn nót chép vào trang sổ này... »
                                </div>
                                
                                <div id="writtenWord1" class="hidden p-2 rounded bg-black/30 border-l-2 border-amber-400 animate-fade-in">
                                    <div class="flex items-baseline justify-between">
                                        <span class="font-serif font-bold text-amber-200 text-sm md:text-base">1. La Liberté</span>
                                        <span class="text-xs text-amber-400/90 font-serif italic">[Tự do]</span>
                                    </div>
                                    <p class="text-[11px] text-slate-300 font-light mt-0.5 leading-snug">
                                        "Tự do không thể là ân huệ đi xin, tự do phải do chính bàn tay nhân dân tự giành lấy."
                                    </p>
                                </div>

                                <div id="writtenWord2" class="hidden p-2 rounded bg-black/30 border-l-2 border-amber-400 animate-fade-in">
                                    <div class="flex items-baseline justify-between">
                                        <span class="font-serif font-bold text-amber-200 text-sm md:text-base">2. L'Égalité</span>
                                        <span class="text-xs text-amber-400/90 font-serif italic">[Bình đẳng]</span>
                                    </div>
                                    <p class="text-[11px] text-slate-300 font-light mt-0.5 leading-snug">
                                        "Họ rêu rao bình đẳng ở chính quốc, nhưng sang thuộc địa lại đối xử với ta như trâu ngựa."
                                    </p>
                                </div>

                                <div id="writtenWord3" class="hidden p-2 rounded bg-black/30 border-l-2 border-amber-400 animate-fade-in">
                                    <div class="flex items-baseline justify-between">
                                        <span class="font-serif font-bold text-amber-200 text-sm md:text-base">3. La Fraternité</span>
                                        <span class="text-xs text-amber-400/90 font-serif italic">[Bác ái]</span>
                                    </div>
                                    <p class="text-[11px] text-slate-300 font-light mt-0.5 leading-snug">
                                        "Bác ái chân chính: Lao động nghèo khổ khắp năm châu bốn biển đều là anh em một nhà."
                                    </p>
                                </div>

                                <div id="writtenWord4" class="hidden p-2 rounded bg-black/30 border-l-2 border-amber-400 animate-fade-in">
                                    <div class="flex items-baseline justify-between">
                                        <span class="font-serif font-bold text-amber-200 text-sm md:text-base">4. La Patrie</span>
                                        <span class="text-xs text-amber-400/90 font-serif italic">[Tổ quốc]</span>
                                    </div>
                                    <p class="text-[11px] text-slate-300 font-light mt-0.5 leading-snug">
                                        "Tổ quốc Việt Nam luôn cháy bỏng trong tim. Đi ngàn dặm chỉ vì một ngày non sông độc lập."
                                    </p>
                                </div>

                                <div id="writtenWord5" class="hidden p-2 rounded bg-black/30 border-l-2 border-amber-400 animate-fade-in">
                                    <div class="flex items-baseline justify-between">
                                        <span class="font-serif font-bold text-amber-200 text-sm md:text-base">5. Le Peuple</span>
                                        <span class="text-xs text-amber-400/90 font-serif italic">[Nhân dân]</span>
                                    </div>
                                    <p class="text-[11px] text-slate-300 font-light mt-0.5 leading-snug">
                                        "Nhân dân là gốc, là sức mạnh dời non lấp biển. Mọi cuộc đấu tranh đều vì hạnh phúc nhân dân."
                                    </p>
                                </div>
                            </div>

                            <!-- Anh Ba's Spoken Insight Quote Box -->
                            <div class="mt-2 p-2.5 rounded-lg bg-amber-950/40 border border-amber-600/40 flex items-start gap-2.5">
                                <div class="w-7 h-7 rounded-full bg-amber-600/30 border border-amber-400 flex items-center justify-center shrink-0 text-xs">
                                    👤
                                </div>
                                <div class="text-left">
                                    <span class="text-[10px] font-cinematic uppercase tracking-widest text-amber-400 font-bold block">
                                        Lời Anh Ba Tâm Sự:
                                    </span>
                                    <p id="studyAnhBaInsight" class="text-xs text-amber-100 font-serif italic leading-relaxed">
                                        "Mỗi tối tôi tranh thủ học vài từ. Viết lên tay, viết lên sàn tàu để nhớ. Muốn đánh đổ xiềng xích, trước hết phải hiểu rõ kẻ thù!"
                                    </p>
                                </div>
                            </div>

                        </div>

                        <!-- Right: 5 Vocabulary Word Action Cards (col-span-5) -->
                        <div class="md:col-span-5 flex flex-col justify-between gap-2">
                            <span class="text-[10px] font-cinematic uppercase tracking-wider text-amber-300/80 font-bold block px-1">
                                Nhấp chọn từ để học và ghi chép:
                            </span>

                            <div class="space-y-2 flex-1">
                                <!-- Word 1 -->
                                <button id="btnStudyWord1" onclick="learnWord(1, 'La Liberté', 'Tự do', 'Tự do không thể là ân huệ đi xin, tự do phải do chính bàn tay nhân dân tự giành lấy.')"
                                        class="w-full p-2.5 rounded-xl border border-amber-500/50 bg-black/60 hover:bg-amber-900/40 hover:border-amber-400 text-left transition flex items-center justify-between cursor-pointer group">
                                    <div>
                                        <span class="font-serif font-bold text-amber-200 text-sm group-hover:text-amber-100">La Liberté</span>
                                        <span class="text-xs text-slate-400 block font-typewriter">Tự do</span>
                                    </div>
                                    <span id="studyWordStatus1" class="text-[10px] font-typewriter px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                        Học từ này →
                                    </span>
                                </button>

                                <!-- Word 2 -->
                                <button id="btnStudyWord2" onclick="learnWord(2, 'L\'Égalité', 'Bình đẳng', 'Họ rêu rao bình đẳng ở chính quốc, nhưng sang thuộc địa lại đối xử với ta như trâu ngựa.')"
                                        class="w-full p-2.5 rounded-xl border border-amber-500/50 bg-black/60 hover:bg-amber-900/40 hover:border-amber-400 text-left transition flex items-center justify-between cursor-pointer group">
                                    <div>
                                        <span class="font-serif font-bold text-amber-200 text-sm group-hover:text-amber-100">L'Égalité</span>
                                        <span class="text-xs text-slate-400 block font-typewriter">Bình đẳng</span>
                                    </div>
                                    <span id="studyWordStatus2" class="text-[10px] font-typewriter px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                        Học từ này →
                                    </span>
                                </button>

                                <!-- Word 3 -->
                                <button id="btnStudyWord3" onclick="learnWord(3, 'La Fraternité', 'Bác ái', 'Bác ái chân chính: Lao động nghèo khổ khắp năm châu bốn biển đều là anh em một nhà.')"
                                        class="w-full p-2.5 rounded-xl border border-amber-500/50 bg-black/60 hover:bg-amber-900/40 hover:border-amber-400 text-left transition flex items-center justify-between cursor-pointer group">
                                    <div>
                                        <span class="font-serif font-bold text-amber-200 text-sm group-hover:text-amber-100">La Fraternité</span>
                                        <span class="text-xs text-slate-400 block font-typewriter">Bác ái</span>
                                    </div>
                                    <span id="studyWordStatus3" class="text-[10px] font-typewriter px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                        Học từ này →
                                    </span>
                                </button>

                                <!-- Word 4 -->
                                <button id="btnStudyWord4" onclick="learnWord(4, 'La Patrie', 'Tổ quốc', 'Tổ quốc Việt Nam luôn cháy bỏng trong tim. Đi ngàn dặm chỉ vì một ngày non sông độc lập.')"
                                        class="w-full p-2.5 rounded-xl border border-amber-500/50 bg-black/60 hover:bg-amber-900/40 hover:border-amber-400 text-left transition flex items-center justify-between cursor-pointer group">
                                    <div>
                                        <span class="font-serif font-bold text-amber-200 text-sm group-hover:text-amber-100">La Patrie</span>
                                        <span class="text-xs text-slate-400 block font-typewriter">Tổ quốc</span>
                                    </div>
                                    <span id="studyWordStatus4" class="text-[10px] font-typewriter px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                        Học từ này →
                                    </span>
                                </button>

                                <!-- Word 5 -->
                                <button id="btnStudyWord5" onclick="learnWord(5, 'Le Peuple', 'Nhân dân', 'Nhân dân là gốc, là sức mạnh dời non lấp biển. Mọi cuộc đấu tranh đều vì hạnh phúc nhân dân.')"
                                        class="w-full p-2.5 rounded-xl border border-amber-500/50 bg-black/60 hover:bg-amber-900/40 hover:border-amber-400 text-left transition flex items-center justify-between cursor-pointer group">
                                    <div>
                                        <span class="font-serif font-bold text-amber-200 text-sm group-hover:text-amber-100">Le Peuple</span>
                                        <span class="text-xs text-slate-400 block font-typewriter">Nhân dân</span>
                                    </div>
                                    <span id="studyWordStatus5" class="text-[10px] font-typewriter px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                        Học từ này →
                                    </span>
                                </button>
                            </div>

                            <!-- Finished Study Button -->
                            <div id="studyCompletionBox" class="hidden mt-2 p-3 rounded-xl bg-gradient-to-r from-emerald-950/90 to-amber-950/90 border border-emerald-500 text-center animate-fade-in">
                                <span class="text-[11px] font-cinematic font-bold text-emerald-300 uppercase block mb-1">
                                    ⭐ Đã Hoàn Thành Bài Học Đêm Khuya ⭐
                                </span>
                                <button id="btnFinishStudy" onclick="finishStudyScene()"
                                        class="w-full py-2 px-4 rounded-lg bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-black font-cinematic font-bold text-xs uppercase tracking-wider shadow-lg transition active:scale-95 cursor-pointer">
                                    Tiếp Tục Hải Trình Ra Thế Giới →
                                </button>
                            </div>

                        </div>

                    </div>

                    <!-- Rig Footer Status -->
                    <div class="mt-3 pt-2 border-t border-[#8c6d48]/30 flex items-center justify-between text-[11px] font-typewriter text-slate-400">
                        <span class="text-amber-300/80">"Không biết tiếng Pháp thì làm sao hiểu được họ..." — Nguyễn Tất Thành</span>
                        <span class="text-amber-400 font-cinematic uppercase">Cabin Tàu Latouche-Tréville • 1911</span>
                    </div>

                </div>
            </div>

            <!-- ---------------------------------------------------- -->
            <!-- 2.75. CẢNH 1: BƯỚC XUỐNG TÀU (KHÔNG HỘP THOẠI) -->
            <!-- ---------------------------------------------------- -->
            <div id="marseilleNoDialogueCard" class="hidden absolute bottom-6 inset-x-4 md:inset-x-auto md:left-1/2 md:-translate-x-1/2 md:max-w-2xl z-30 pointer-events-auto">
                <div class="p-4 md:p-5 rounded-2xl bg-[#070c18]/90 border border-amber-400/50 backdrop-blur-md shadow-[0_20px_50px_rgba(0,0,0,0.9)] text-center space-y-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/15 border border-amber-400/40 text-amber-300 font-cinematic text-[11px] font-bold tracking-widest uppercase">
                        ⚓ 06.07.1911 • CẢNG MARSEILLE (NƯỚC PHÁP)
                    </span>
                    <p class="font-cinematic text-sm md:text-base text-slate-100 font-medium leading-relaxed">
                        Sau 1 tháng 1 ngày vượt trùng dương mênh mông, con tàu Amiral Latouche-Tréville hạ cầu tàu gỗ cập bến Marseille. Dòng người hành khách và thủy thủ bắt đầu bước chân xuống đất Pháp...
                    </p>
                    <div class="pt-1 flex items-center justify-center gap-2 text-xs font-typewriter text-amber-300/80">
                        <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
                        <button onclick="advanceDialogue()" class="hover:text-amber-200 underline underline-offset-4 cursor-pointer">
                            Nhấp vào đây hoặc bấm [Space] để tiếp tục quan sát →
                        </button>
                    </div>
                </div>
            </div>

            <!-- ---------------------------------------------------- -->
            <!-- 2.8. CẢNG MARSEILLE: TRẠM ĐIỀU HƯỚNG KHÔNG GIAN 3 HƯỚNG -->
            <!-- ---------------------------------------------------- -->
            <div id="diegeticMarseilleRig" class="hidden absolute inset-0 pointer-events-auto select-none z-25 flex flex-col justify-between p-4 md:p-6">
                
                <!-- Header Status Banner -->
                <div class="w-full max-w-4xl mx-auto flex items-center justify-between p-3 rounded-xl bg-[#070c18]/90 border border-sky-500/40 backdrop-blur-md shadow-xl">
                    <div class="flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-sky-950/90 border border-sky-400/60 flex items-center justify-center text-sky-300 text-sm">
                            ⚓
                        </div>
                        <div>
                            <span class="text-[9px] uppercase font-typewriter text-sky-400 tracking-widest block font-bold">
                                BẾN CẢNG VIEUX-PORT • MARSEILLE (PHÁP) • 06.07.1911
                            </span>
                            <h3 id="marseilleSpatialTitle" class="font-cinematic text-xs md:text-sm font-bold text-slate-100 uppercase tracking-wider">
                                Quảng Trường Cảng: Chọn Hướng Quan Sát Đời Sống
                            </h3>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <span id="marseilleExplorationBadge" class="px-3 py-1 rounded-full bg-black/70 border border-sky-500/50 text-sky-300 font-typewriter text-xs font-bold">
                            0 / 2 Hướng Khám Phá
                        </span>
                    </div>
                </div>

                <!-- Central Navigation Arrows (Visible when in Center) -->
                <div id="marseilleCenterNav" class="w-full max-w-5xl mx-auto flex items-center justify-between my-auto px-2">
                    <!-- Left Button -->
                    <button id="btnPanLeft" onclick="panToMarseilleView('left')"
                            class="group p-4 md:p-5 rounded-2xl bg-[#070c18]/90 hover:bg-sky-950/80 border-2 border-sky-500/50 hover:border-amber-400 backdrop-blur-md shadow-[0_15px_35px_rgba(0,0,0,0.8)] transition-all transform hover:-translate-x-2 cursor-pointer flex flex-col items-start gap-1 max-w-[260px] md:max-w-xs text-left">
                        <div class="flex items-center gap-2 text-amber-300 font-cinematic font-bold text-xs uppercase tracking-wider">
                            <span class="text-base group-hover:scale-125 transition-transform">←</span>
                            <span>HƯỚNG TRÁI</span>
                        </div>
                        <h4 class="font-body font-bold text-sm text-slate-100 group-hover:text-amber-200">
                            Hàng Phu Kéo Xe Da Trắng
                        </h4>
                        <p class="text-[11px] text-slate-300 font-light leading-snug">
                            Quan sát những người lao động Pháp nghèo khổ còng lưng kéo xe hàng nặng trĩu.
                        </p>
                        <span id="marseilleLeftStatus" class="mt-2 text-[10px] font-typewriter px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 border border-sky-500/30">
                            Chưa quan sát
                        </span>
                    </button>

                    <!-- Center Compass Hint -->
                    <div class="hidden md:flex flex-col items-center justify-center p-3 rounded-full bg-black/60 border border-sky-500/30 backdrop-blur-sm text-center">
                        <span class="text-xs text-sky-300 font-typewriter uppercase tracking-widest font-bold">La Bàn Quan Sát</span>
                        <span class="text-[10px] text-slate-400">Chọn 2 hướng để tìm ra Chân Lý</span>
                    </div>

                    <!-- Right Button -->
                    <button id="btnPanRight" onclick="panToMarseilleView('right')"
                            class="group p-4 md:p-5 rounded-2xl bg-[#070c18]/90 hover:bg-sky-950/80 border-2 border-sky-500/50 hover:border-amber-400 backdrop-blur-md shadow-[0_15px_35px_rgba(0,0,0,0.8)] transition-all transform hover:translate-x-2 cursor-pointer flex flex-col items-end gap-1 max-w-[260px] md:max-w-xs text-right">
                        <div class="flex items-center gap-2 text-amber-300 font-cinematic font-bold text-xs uppercase tracking-wider">
                            <span>HƯỚNG PHẢI</span>
                            <span class="text-base group-hover:scale-125 transition-transform">→</span>
                        </div>
                        <h4 class="font-body font-bold text-sm text-slate-100 group-hover:text-amber-200">
                            Bậc Đá Cảng Cũ & Người Nghèo
                        </h4>
                        <p class="text-[11px] text-slate-300 font-light leading-snug">
                            Chứng kiến những người phụ nữ, trẻ em và người già ăn xin cơ hàn bên bờ đá.
                        </p>
                        <span id="marseilleRightStatus" class="mt-2 text-[10px] font-typewriter px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 border border-sky-500/30">
                            Chưa quan sát
                        </span>
                    </button>
                </div>

                <!-- Left Focused Panel (When in Left View) -->
                <div id="marseilleLeftPanel" class="hidden w-full max-w-3xl mx-auto my-auto p-5 md:p-6 rounded-2xl bg-[#070c18]/95 border-2 border-amber-500/60 backdrop-blur-md shadow-2xl animate-fade-in space-y-3">
                    <div class="flex items-center justify-between border-b border-amber-500/30 pb-2">
                        <span class="text-xs font-cinematic font-bold text-amber-300 uppercase tracking-wider flex items-center gap-2">
                            <span>←</span> GÓC QUAN SÁT PHÍA TRÁI: HÀNG PHU KÉO XE
                        </span>
                        <span class="text-[10px] font-cinematic px-2.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                            ✓ ĐÃ QUAN SÁT
                        </span>
                    </div>
                    <div class="space-y-2">
                        <h3 class="font-body font-bold text-base md:text-lg text-slate-100">
                            Người Pháp Da Trắng Lao Động Cực Nhọc Chẳng Khác Gì Xứ Ta
                        </h3>
                        <p class="font-body text-xs md:text-sm text-slate-300 leading-relaxed">
                            Dưới nắng hè gay gắt của vịnh Địa Trung Hải, những người thợ khuân vác và phu xe Pháp còng lưng kéo từng chuyến xe hàng nặng trĩu. Mồ hôi nhễ nhại ướt đẫm áo vải thô, nét mặt hằn sâu nỗi vất vả mưu sinh.
                        </p>
                        <div class="p-3 rounded-xl bg-amber-950/40 border-l-4 border-amber-400 text-xs md:text-sm text-amber-200 font-body italic leading-relaxed">
                            <strong class="text-amber-300 not-italic">Anh Ba trầm ngâm chia sẻ:</strong> "Anh nhìn kìa... Ngay tại chính quốc, người Pháp da trắng cũng phải kéo xe, mồ hôi nhễ nhại, cực nhọc chẳng khác gì phu xe An Nam ta! Họ cũng phải bán sức lao động để kiếm miếng cơm manh áo."
                        </div>
                    </div>
                    <div class="pt-2 text-center">
                        <button onclick="panToMarseilleView('center')"
                                class="py-2.5 px-6 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-cinematic font-bold text-xs uppercase tracking-wider shadow-lg transition active:scale-95 cursor-pointer">
                            Quay Về Giữa Bến Cảng →
                        </button>
                    </div>
                </div>

                <!-- Right Focused Panel (When in Right View) -->
                <div id="marseilleRightPanel" class="hidden w-full max-w-3xl mx-auto my-auto p-5 md:p-6 rounded-2xl bg-[#070c18]/95 border-2 border-amber-500/60 backdrop-blur-md shadow-2xl animate-fade-in space-y-3">
                    <div class="flex items-center justify-between border-b border-amber-500/30 pb-2">
                        <span class="text-xs font-cinematic font-bold text-amber-300 uppercase tracking-wider flex items-center gap-2">
                            GÓC QUAN SÁT PHÍA PHẢI: BẬC ĐÁ CẢNG CŨ <span>→</span>
                        </span>
                        <span class="text-[10px] font-cinematic px-2.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                            ✓ ĐÃ QUAN SÁT
                        </span>
                    </div>
                    <div class="space-y-2">
                        <h3 class="font-body font-bold text-base md:text-lg text-slate-100">
                            Nỗi Khổ Cực & Phận Nghèo Bên Bờ Biển Mẫu Quốc
                        </h3>
                        <p class="font-body text-xs md:text-sm text-slate-300 leading-relaxed">
                            Bên mép nước bến cảng, những bậc đá cũ rêu phong là nơi co ro của những người phụ nữ bế con nhỏ và người già ăn xin. Ảo tưởng về một "thiên đường văn minh giàu sang đồng đều" của chế độ thực dân tan vỡ hoàn toàn.
                        </p>
                        <div class="p-3 rounded-xl bg-amber-950/40 border-l-4 border-amber-400 text-xs md:text-sm text-amber-200 font-body italic leading-relaxed">
                            <strong class="text-amber-300 not-italic">Anh Ba mắt thoáng buồn:</strong> "Tại sao thực dân rêu rao sang xứ ta để 'khai hóa', trong khi ngay trên đất nước họ, những người lao động nghèo khổ vẫn phải sống cảnh bần hàn đói rách thế này?!"
                        </div>
                    </div>
                    <div class="pt-2 text-center">
                        <button onclick="panToMarseilleView('center')"
                                class="py-2.5 px-6 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-cinematic font-bold text-xs uppercase tracking-wider shadow-lg transition active:scale-95 cursor-pointer">
                            ← Quay Về Giữa Bến Cảng
                        </button>
                    </div>
                </div>

                <!-- Epiphany Embossed Overlay (When returned to Center after exploring both) -->
                <div id="marseilleEpiphanyOverlay" class="hidden absolute inset-0 bg-black/90 backdrop-blur-md z-30 flex flex-col items-center justify-center p-6 text-center animate-fade-in">
                    <div class="max-w-3xl space-y-4">
                        <div class="inline-flex items-center gap-2 px-4 py-1 rounded-full bg-amber-500/20 border border-amber-400/50 text-amber-300 font-cinematic text-xs font-bold uppercase tracking-widest shadow-lg">
                            ⭐ BƯỚC NGOẶT TƯ TƯỞNG TẠI CẢNG MARSEILLE • 06.07.1911 ⭐
                        </div>

                        <p class="font-cinematic text-lg md:text-2xl text-amber-200 font-bold uppercase tracking-wide drop-shadow-[0_4px_16px_rgba(245,158,11,0.6)]">
                            "Ở Pháp cũng có những người nghèo như ở xứ ta..."
                        </p>

                        <h2 class="font-cinematic text-2xl md:text-4xl text-white font-black uppercase tracking-wide leading-tight drop-shadow-[0_6px_25px_rgba(0,0,0,1)]">
                            KẺ THÙ LÀ ÁCH ÁP BỨC THỰC DÂN,<br>
                            <span class="text-amber-400">CÒN NHÂN DÂN LAO ĐỘNG PHÁP CHÍNH LÀ BẠN BÈ!</span>
                        </h2>

                        <p class="font-body text-xs md:text-sm text-slate-300 italic max-w-2xl mx-auto leading-relaxed">
                            Lần đầu tiên trong lịch sử cách mạng Việt Nam, người thanh niên Nguyễn Tất Thành đã phân biệt rõ ràng giữa nhân dân lao động Pháp và chính quyền thực dân cai trị. Đây là viên gạch nền móng đầu tiên cho tư tưởng đoàn kết quốc tế cao đẹp.
                        </p>

                        <div class="pt-6">
                            <button id="btnFinishEpiphany" onclick="finishMarseilleSpatialScene()"
                                    class="py-3 px-8 rounded-xl bg-gradient-to-r from-amber-500 via-orange-500 to-amber-500 hover:from-amber-400 hover:to-orange-400 text-black font-cinematic font-bold text-sm uppercase tracking-wider shadow-[0_0_35px_rgba(245,158,11,0.8)] transition active:scale-95 cursor-pointer animate-bounce">
                                Tiếp Tục Hải Trình Ra Thế Giới (Sang Hoa Kỳ 1912) →
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Footer status bar -->
                <div class="w-full max-w-4xl mx-auto flex items-center justify-between text-[11px] font-typewriter text-slate-400 pt-2 border-t border-sky-500/20">
                    <span id="marseilleInsightText" class="text-sky-300/80 font-body">"Người Pháp ở Pháp tốt và lịch sự hơn thực dân ở xứ ta rất nhiều..." — Văn Ba</span>
                    <span class="text-sky-400 font-cinematic uppercase">Cảng Marseille • Tháng 7/1911</span>
                </div>

            </div>

            <!-- ---------------------------------------------------- -->
            <!-- 3. HƯƠNG CẢNG 1930: 3 HUY HIỆU HỢP NHẤT TRÊN BÀN HỘI NGHỊ -->
            <!-- ---------------------------------------------------- -->
            <div id="diegeticUnificationRig" class="hidden absolute inset-0 pointer-events-auto select-none flex flex-col items-center justify-center p-4">
                <div class="w-full max-w-xl bg-void/95 border-2 border-amber-500/70 rounded-xl p-5 shadow-2xl text-center backdrop-blur-md">
                    <span class="text-[10px] font-cinematic uppercase tracking-widest text-amber-400 font-bold block mb-1">
                        HỘI NGHỊ HỢP NHẤT • HƯƠNG CẢNG (03.02.1930)
                    </span>
                    <h3 class="font-cinematic text-lg font-bold text-amber-100 uppercase tracking-wider">
                        Hợp Nhất Các Tổ Chức Cộng Sản Thành Một Đảng Duy Nhất
                    </h3>
                    <p class="text-xs text-slate-300 font-light mt-1 mb-4">
                        Nhấp vào các tổ chức cộng sản để hợp nhất thành <strong>Đảng Cộng sản Việt Nam</strong>!
                    </p>

                    <div class="flex items-center justify-center gap-3">
                        <button id="badge1" onclick="unifyBadge(1)" class="p-3 rounded-lg bg-stone-900 border border-amber-500/50 hover:border-amber-400 text-xs font-typewriter text-amber-200 transition cursor-pointer">
                            Đông Dương<br>Cộng sản Đảng
                        </button>
                        <button id="badge2" onclick="unifyBadge(2)" class="p-3 rounded-lg bg-stone-900 border border-amber-500/50 hover:border-amber-400 text-xs font-typewriter text-amber-200 transition cursor-pointer">
                            An Nam<br>Cộng sản Đảng
                        </button>
                        <button id="badge3" onclick="unifyBadge(3)" class="p-3 rounded-lg bg-stone-900 border border-amber-500/50 hover:border-amber-400 text-xs font-typewriter text-amber-200 transition cursor-pointer">
                            Đông Dương<br>Cộng sản Liên đoàn
                        </button>
                    </div>

                    <!-- Unified CPV Crest -->
                    <div id="unifiedCrest" class="hidden mt-4 p-3 rounded-xl bg-red-950/80 border-2 border-red-500 text-amber-300 font-cinematic font-bold text-sm uppercase tracking-widest animate-pulse">
                        ⭐ ĐẢNG CỘNG SẢN VIỆT NAM RA ĐỜI (03.02.1930) ⭐
                    </div>
                </div>
            </div>

            <!-- ---------------------------------------------------- -->
            <!-- 4. PÁC BÓ 1941: CHẠM CỘT MỐC 108 TRÊN SƯỜN NÚI -->
            <!-- ---------------------------------------------------- -->
            <div id="diegeticMilestoneRig" class="hidden absolute inset-0 pointer-events-auto select-none flex flex-col items-center justify-center p-4">
                <div class="text-center bg-void/90 border border-emerald-500/60 p-5 rounded-2xl backdrop-blur-md shadow-2xl max-w-md">
                    <span class="text-[10px] font-cinematic uppercase tracking-widest text-emerald-400 font-bold block mb-1">
                        PÁC BÓ • NGÀY 28 THÁNG 1 NĂM 1941
                    </span>
                    <h3 class="font-cinematic text-lg font-bold text-white uppercase tracking-wider">
                        Cột Mốc 108 — 30 Năm Trở Về Đất Mẹ
                    </h3>
                    <div id="insceneMilestoneBtn" onclick="touchInsceneMilestone()" 
                         class="my-4 mx-auto w-32 h-44 rounded-t-2xl bg-stone-700 border-4 border-stone-400 flex flex-col items-center justify-center cursor-pointer hover:border-amber-400 hover:scale-105 transition-all shadow-2xl group">
                        <span class="text-2xl font-bold font-typewriter text-amber-300 group-hover:text-amber-200">108</span>
                        <span class="text-[10px] font-typewriter text-slate-300 uppercase mt-1">VIỆT NAM</span>
                        <span class="text-[9px] text-amber-400 mt-2 font-typewriter animate-pulse">Nhấp Chạm →</span>
                    </div>
                    <p id="inscenePoem" class="hidden font-cinematic italic text-xs md:text-sm text-amber-200 mt-2 animate-fade-in">
                        "Kìa, bóng Bác đang hôn lên hòn đá<br>Lắng nghe trong màu hồng sắc đỏ quê hương..."
                    </p>
                </div>
            </div>

            <!-- ---------------------------------------------------- -->
            <!-- 5. VĨ THANH: NGỌN ĐÈN NỞ BÌNH MINH ĐỘC LẬP -->
            <!-- ---------------------------------------------------- -->
            <div id="diegeticDawnRig" class="hidden absolute inset-0 pointer-events-auto select-none flex flex-col items-center justify-center p-4">
                <div class="text-center bg-void/95 border-2 border-amber-400 p-6 md:p-8 rounded-2xl backdrop-blur-lg shadow-[0_0_80px_rgba(245,158,11,0.6)] max-w-xl animate-fade-in">
                    <span class="px-3.5 py-1.5 rounded-full bg-amber-500/20 border border-amber-400 text-amber-300 text-xs font-cinematic uppercase tracking-widest font-bold mb-3 inline-block">
                        VĨ THANH KHẢI HOÀN • TƯ TƯỞNG HỒ CHÍ MINH
                    </span>
                    <h2 class="text-2xl md:text-3xl font-bold font-cinematic text-amber-100 tracking-wide">
                        Từ Ngọn Đèn Dầu 1911 Đến Bình Minh Độc Lập
                    </h2>
                    <blockquote class="font-cinematic text-sm md:text-base text-amber-200 italic border-l-4 border-amber-400 pl-3 my-3 text-left">
                        "Không có gì quý hơn độc lập, tự do!"<br>
                        "Độc lập dân tộc gắn liền với Chủ nghĩa xã hội."
                    </blockquote>
                    <p class="text-slate-400 text-xs font-typewriter mt-2">
                        Thiên sử thi 30 năm (1911 – 1941) đã đưa non sông Việt Nam bước vào kỷ nguyên độc lập, tự do và phồn vinh.
                    </p>
                    <div class="flex items-center justify-center gap-3 mt-4">
                        <button onclick="toggleLogModal(true)" class="px-4 py-2 rounded-xl border border-brass/40 bg-abyss text-brass font-cinematic font-bold text-xs uppercase cursor-pointer">
                            Xem Nhật Ký Hải Trình
                        </button>
                        <button onclick="restartExperience()" class="px-5 py-2 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 text-black font-cinematic font-bold text-xs uppercase shadow-lg cursor-pointer">
                            Chơi Lại Từ Đầu [R]
                        </button>
                    </div>
                </div>
            </div>

        </div>

        <!-- ========================================== -->
        <!-- DIALOGUE & KINETIC SUBTITLE FOOTER -->
        <!-- ========================================== -->
        <main class="hud-element relative z-20 p-4 md:p-6 flex flex-col justify-end w-full max-w-5xl mx-auto pointer-events-none">
            <div class="w-full flex flex-col gap-3 pointer-events-auto">
                
                <!-- Branching Choices -->
                <div id="choicesContainer" class="hidden flex flex-col gap-2 mb-1 animate-fade-in">
                    <span class="text-[11px] font-typewriter text-amber-300/90 tracking-wider uppercase flex items-center gap-1.5 px-1">
                        <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                        Lựa chọn đồng hành của bạn:
                    </span>
                    <div id="choicesList" class="grid grid-cols-1 md:grid-cols-2 gap-2.5"></div>
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
                                Bến Nhà Rồng • 05/06/1911
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
                            <span id="stepActSummary">Hồi 1/6:</span>
                            <span id="stepSceneTitle" class="text-slate-200 font-semibold">Lời Thề Gác Trọ</span>
                        </div>
                        <div id="stepIndicator" class="font-typewriter text-brass font-bold">1 / 24</div>
                    </div>
                </div>

            </div>
        </main>

        <!-- ======================================================== -->
        <!-- HỒI 0: DẪN NHẬP LỊCH SỬ (PROLOGUE) -->
        <!-- ======================================================== -->
        <audio id="prologueBgmAudio" preload="auto" loop class="hidden">
            <source src="prologue_theme.mp3" type="audio/mpeg">
            <source src="prologue_theme.ogg" type="audio/ogg">
        </audio>

        <div id="prologueStage" onclick="handlePrologueBackgroundClick(event)" class="absolute inset-0 z-[60] bg-black flex flex-col justify-between p-4 md:p-8 transition-opacity duration-1000 overflow-hidden select-none cursor-pointer">
            <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
                <img id="prologueBgImg" src="prologue_1_can_vuong.jpg" alt="Minh họa lịch sử Hồi 0" 
                     class="w-full h-full object-cover object-center filter brightness-[0.92] contrast-105 transition-all duration-700 transform scale-100 kenburns-1">
                <canvas id="prologueVfxCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-[1]"></canvas>
                <div class="absolute inset-x-0 bottom-0 h-80 bg-gradient-to-t from-black via-black/70 to-transparent z-[2]"></div>
                <div class="absolute inset-x-0 top-0 h-28 bg-gradient-to-b from-black/80 to-transparent z-[2]"></div>
            </div>

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

                <div id="audioStartHint" class="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-amber-500/15 border border-amber-400/40 text-amber-300 text-[11px] font-typewriter backdrop-blur-md animate-pulse shadow-md">
                    <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>
                    <span>Nhấp chuột hoặc [Space] để mở nhạc nền dương cầm</span>
                </div>

                <button onclick="event.stopPropagation(); skipPrologue()" class="min-h-[44px] px-4 py-2 rounded-lg border border-white/20 bg-black/50 hover:bg-black/80 backdrop-blur-md text-slate-200 hover:text-white text-xs font-typewriter transition-all cursor-pointer">
                    <span>Bỏ qua dẫn nhập</span> <span class="text-[10px] text-slate-400 hidden sm:inline">[Esc]</span>
                </button>
            </div>

            <div class="relative z-10 w-full max-w-5xl mx-auto pb-4 md:pb-8 pointer-events-auto">
                <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                        <span id="prologueEraBadge" class="text-xs md:text-sm font-typewriter text-amber-400 tracking-widest font-semibold uppercase flex items-center gap-2 drop-shadow-[0_2px_4px_rgba(0,0,0,1)]">
                            <span class="w-2 h-2 rounded-full bg-amber-400 shadow-[0_0_8px_rgba(245,158,11,1)]"></span>
                            <span id="prologueEraText">1885 – 1908 • ĐÊM DÀI NÔ LỆ</span>
                        </span>
                        <div class="flex items-center gap-1.5" id="prologueDots"></div>
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
                            <span class="text-xs text-slate-300/80 font-typewriter hidden sm:inline">Nhấp màn hình / [Space] để tiếp tục</span>
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
        <!-- MENU CÁC HỒI KÝ LỊCH SỬ (CHAPTER SELECT MODAL) -->
        <!-- ======================================================== -->
        <div id="chapterMenuModal" class="hidden absolute inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
            <div class="max-w-2xl w-full bg-abyss border border-brass/60 rounded-2xl p-6 flex flex-col shadow-2xl">
                <div class="flex items-center justify-between pb-3 mb-4 border-b border-brass/30">
                    <h3 class="font-cinematic text-lg font-bold text-brass uppercase tracking-wider flex items-center gap-2">
                        <svg class="w-5 h-5 text-brass" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                        Danh Mục 6 Hồi Ký Hải Trình (1911 – 1941)
                    </h3>
                    <button onclick="toggleChapterMenu(false)" class="p-2 text-slate-400 hover:text-white cursor-pointer">
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
                    <button onclick="jumpToChapter('inn_1')" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 1 • LỜI THỀ GÁC TRỌ (06/1911)</span>
                            <span class="text-slate-400 text-[11px]">Căn Gác Trọ Sài Gòn, Hai Bàn Tay & Lời Thề Khởi Hành</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter('dock_1')" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 2 • XUẤT BẾN BẾN NHÀ RỒNG (05.06.1911)</span>
                            <span class="text-slate-400 text-[11px]">Ký Sổ Thuyền Viên Phụ Bếp & Còi Tàu Nhổ Neo</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter('ship_1')" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 3 • GIAN LAO HẢI TRÌNH & VÒNG QUANH THẾ GIỚI (1911 – 1917)</span>
                            <span class="text-slate-400 text-[11px]">Xúc Than Hầm Lò 40°C, Sổ Tay Boong Tàu, Cảng Marseille, Boston & London</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter('act4_1')" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 4 • TỎA SÁNG CHÂN LÝ CỨU NƯỚC (1917 – 1923)</span>
                            <span class="text-slate-400 text-[11px]">Yêu Sách Versailles 1919, Viên Gạch Hồng & Luận Cương Lênin, Đại Hội Tours</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter('act5_1')" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 5 • NGỌN LỬA LAN TỎA CÁCH MẠNG (1923 – 1930)</span>
                            <span class="text-slate-400 text-[11px]">Mát-xcơ-va, Đường Kách Mệnh Quảng Châu & Hợp Nhất Đảng Tại Hương Cảng</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                    <button onclick="jumpToChapter('act6_1')" class="w-full text-left p-3 rounded-xl border border-slate-700 bg-void/80 hover:border-brass hover:bg-brass/10 flex items-center justify-between transition cursor-pointer">
                        <div>
                            <span class="text-amber-400 font-bold block">HỒI 6 • MÙA XUÂN TRỞ VỀ & BÌNH MINH NON SÔNG (1941)</span>
                            <span class="text-slate-400 text-[11px]">Cột Mốc 108 Pác Bó, Bàn Đá Cốc Bó & Bình Minh Độc Lập</span>
                        </div>
                        <span class="text-brass">Khám phá →</span>
                    </button>
                </div>
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
                        Nhật Ký Hải Trình 30 Năm (1911 – 1941)
                    </h3>
                    <button onclick="toggleLogModal(false)" class="p-2 rounded text-slate-400 hover:text-white cursor-pointer">
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
    <!-- JAVASCRIPT: THE COMPLETE 6-ACT EPIC ENGINE (24 STEPS) -->
    <!-- ======================================================== -->
    <script>
        /* ----------------------------------------------------
         * 1. 6-ACT MASTER EPIC SCRIPT (24 STEPS)
         * ---------------------------------------------------- */
        const SCENE_SCRIPT = [
            // === HỒI 1: LỜI THỀ GÁC TRỌ (SÀI GÒN, ĐẦU THÁNG 6/1911) ===
            {
                id: 'inn_1',
                image: 'inn_1_talking.jpg',
                act: 'HỒI 1 • LỜI THỀ GÁC TRỌ',
                actIndex: 1,
                sceneNum: 'Cảnh 1/4',
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
                sceneNum: 'Cảnh 2/4',
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
                sceneNum: 'Cảnh 3/4',
                location: 'Căn Gác Trọ Nhỏ — Sài Gòn',
                coords: '10°46\'N 106°42\'E • Đầu Tháng 06/1911 (Đêm)',
                speaker: 'Văn Ba',
                role: 'Xòe rộng hai bàn tay rắn rỏi trước ngọn đèn dầu',
                text: 'Đây, tiền đây! Chúng ta sẽ làm việc. Chúng ta sẽ làm bất cứ việc gì để sống và để đi. Hai bàn tay này sẽ nuôi sống chúng ta, anh đừng lo lắng! Có lao động, có ý chí thì không gì là không thể vượt qua.',
                action: 'ambient'
            },
            {
                id: 'inn_3',
                image: 'inn_3_handshake.jpg',
                act: 'HỒI 1 • LỜI THỀ GÁC TRỌ',
                actIndex: 1,
                sceneNum: 'Cảnh 4/4',
                location: 'Căn Gác Trọ Nhỏ — Sài Gòn',
                coords: '10°46\'N 106°42\'E • Rạng Sáng 05.06.1911',
                speaker: 'Người Dẫn Truyện',
                role: 'Khoảnh khắc ước hẹn lịch sử',
                text: 'Hai bàn tay siết chặt nhau qua ánh đèn dầu bập bùng. Lời thề son sắt giữa hai người thanh niên yêu nước đã được kết giao trong đêm tối thuộc địa. Bình minh đã hé, bến cảng Sài Gòn đang đón đợi!',
                action: 'ambient'
            },

            // === HỒI 2: XUẤT BẾN BẾN NHÀ RỒNG (12H TRƯA 05.06.1911) ===
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
                action: 'ambient'
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
                text: 'Tôi đã xin được việc phụ bếp với mức lương 45 quan Pháp một tháng rồi. Cuốn sổ thuyền viên đang mở sẵn ngay trên bàn, anh hãy ghi tên mình vào để chúng ta cùng lên tàu!',
                action: 'diegetic_register'
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
                text: 'Hai người xách túi vải bước lên cầu tàu dốc đứng. Đứng trên lan can sắt, anh Ba ngoái đầu nhìn lại bến cảng quê hương lần cuối... Tiếng còi tàu rền rĩ hú 3 hồi, rẽ sóng ra khơi!',
                action: 'play_horn'
            },

            // === HỒI 3: GIAN LAO HẢI TRÌNH & VÒNG QUANH THẾ GIỚI (1911 – 1917) ===
            {
                id: 'ship_1',
                image: 'ship_1_boiler.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 1/8',
                location: 'Hầm Than Tàu Hơi Nước Amiral Latouche-Tréville',
                coords: 'Ấn Độ Dương • Mùa Hè 1911',
                speaker: 'Văn Ba',
                role: 'Phụ bếp & thợ hầm than (Nhiệt độ > 40°C)',
                text: 'Dưới đáy sâu con tàu, nhiệt độ hầm than vượt quá 40 độ C, bụi than bám đen kịt mặt mũi, mồ hôi chảy ròng ròng cay xè mắt. Áp suất nồi hơi đang sụt giảm nghiêm trọng, ngọn lửa này quyết không được để tắt! Anh bạn, hãy nhấp vào Cửa Lò để giúp tôi tiếp than!',
                action: 'open_boiler_hotspot'
            },
            {
                id: 'ship_1_dialogue',
                image: 'ship_1_boiler.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 2/8',
                location: 'Hầm Than Tàu Hơi Nước',
                coords: 'Ấn Độ Dương • Mùa Hè 1911',
                speaker: 'Văn Ba',
                role: 'Lau vội mồ hôi trên trán bên chảo gang',
                text: 'Làm việc từ 4 giờ sáng đến đêm mịt, rửa nồi, khiêng chảo, xúc than... Nhưng anh thấy không, chỉ có lao động chân chính mới giúp ta hiểu thấu nỗi khổ cực của những người cùng khổ trên khắp thế giới này!',
                action: 'ambient'
            },
            {
                id: 'ship_2',
                image: 'ship_2_study.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 3/8',
                location: 'Góc Cabin Thuyền Viên • Đêm Khuya 1911',
                coords: 'Ấn Độ Dương • Đêm Khuya Mùa Hè 1911',
                speaker: 'Văn Ba',
                role: 'Dưới ánh đèn dầu bão bên bàn gỗ mộc',
                text: 'Sau một ngày dài xúc than và rửa nồi kiệt sức, đây là lúc quý giá nhất để học tập. Muốn hiểu kẻ thù và giải phóng đồng bào, ta nhất định phải làm chủ ngôn ngữ của họ! Hãy cùng tôi nắn nót ghi lại những từ vựng thiêng liêng này vào sổ tay.',
                action: 'diegetic_study'
            },
            {
                id: 'marseille_step_1',
                image: 'marseille_disembark.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 4/8',
                location: 'Cầu Tàu Amiral Latouche-Tréville • Cảng Marseille',
                coords: '43°17\'N 5°22\'E • Trưa 06.07.1911',
                speaker: 'Không Gian',
                role: 'Cầu tàu hạ xuống, dòng người rời tàu sau 1 tháng vượt biển',
                text: 'Ngày 06 tháng 7 năm 1911 — Sau 1 tháng 1 ngày vượt trùng dương mênh mông, con tàu Amiral Latouche-Tréville hạ cầu tàu gỗ cập bến Marseille. Dòng người hành khách và thủy thủ bắt đầu bước chân xuống nước Pháp...',
                action: 'marseille_disembark_no_dialogue'
            },
            {
                id: 'marseille_step_2',
                image: 'marseille_deck_lookout.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 5/8',
                location: 'Trên Mạn Tàu Amiral Latouche-Tréville',
                coords: 'Nhìn xuống bến cảng Marseille • Trưa 06.07.1911',
                speaker: 'Văn Ba',
                role: 'Nguyễn Tất Thành (21 tuổi) đứng tựa lan can mạn tàu, ánh mắt suy tư',
                text: 'Kia là nước Pháp... đất nước của những kẻ đang đè đầu cưỡi cổ nhân dân ta ở quê nhà. Họ luôn miệng rêu rao khẩu hiệu Tự do - Bình đẳng - Bác ái, nhưng hãy nhìn xuống bến cảng xem cuộc sống thực sự của họ như thế nào. Nào, chúng ta cùng xuống tàu!',
                action: 'ambient'
            },
            {
                id: 'marseille_hub',
                image: 'marseille_1_port.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 6/8',
                location: 'Quảng Trường Cảng Cũ Marseille (Vieux-Port)',
                coords: 'Bến Cảng Marseille • Ngày 06.07.1911',
                speaker: 'Văn Ba',
                role: 'Đứng trên bến cảng nhìn về khu dân cư',
                text: 'Chúng ta đã đặt chân lên đất Pháp. Hãy nhìn sang hai hướng bến cảng: bên trái là hàng phu kéo xe da trắng, bên phải là bậc đá cảng cũ nơi người nghèo co ro. Hãy nhấp chọn hướng để quan sát đời sống nhân dân Pháp!',
                action: 'diegetic_marseille_spatial'
            },
            {
                id: 'world_1',
                image: 'world_1_boston_london.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 7/8',
                location: 'Boston & New York (Hoa Kỳ) • 1912 – 1913',
                coords: 'Khách Sạn Parker House, Boston (Mỹ)',
                speaker: 'Người Dẫn Truyện',
                role: 'Quan sát xã hội tư bản phương Tây',
                text: 'Năm 1912–1913, con tàu đưa Người cập cảng Hoa Kỳ. Tại Boston và New York, Bác làm phụ bếp làm bánh ở khách sạn Parker House, đến thăm khu người da đen Harlem, tận mắt chứng kiến sự phân biệt chủng tộc tàn khốc đằng sau bức tượng Nữ thần Tự do.',
                action: 'ambient'
            },
            {
                id: 'world_2',
                image: 'world_1_boston_london.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 8/8',
                location: 'London (Vương Quốc Anh) • 1913 – 1917',
                coords: 'Khách Sạn Carlton, Luân Đôn (Anh)',
                speaker: 'Văn Ba',
                role: 'Quét tuyết mùa đông nước Anh',
                text: 'Mùa đông Luân Đôn giá rét cắt da thịt, tôi đi quét tuyết trong công viên, làm bồi bàn ở khách sạn Carlton... Sống giữa lòng các đế quốc hùng mạnh, tôi càng thấy rõ: ở đâu nhân dân lao động cũng bị bóc lột, và ở đâu chủ nghĩa thực dân cũng tàn bạo như nhau!',
                action: 'ambient'
            },

            // === HỒI 4: TỎA SÁNG CHÂN LÝ CỨU NƯỚC (PARIS 1917 – 1923) ===
            {
                id: 'act4_1',
                image: 'act4_1_versailles_1919.jpg',
                act: 'HỒI 4 • TỎA SÁNG CHÂN LÝ',
                actIndex: 4,
                sceneNum: 'Cảnh 1/4',
                location: 'Hội Nghị Hòa Bình Versailles (Pháp)',
                coords: 'Paris (Pháp) • Ngày 18.06.1919',
                speaker: 'Người Dẫn Truyện',
                role: 'Bản Yêu sách làm chấn động đế quốc Pháp',
                text: 'Ngày 18 tháng 6 năm 1919, thay mặt Hội những người An Nam yêu nước, một thanh niên gầy gò ký tên NGUYỄN ÁI QUỐC gửi tới Hội nghị Versailles "Bản Yêu sách của nhân dân An Nam" gồm 8 điểm, đòi quyền tự do, bình đẳng. Tên tuổi Nguyễn Ái Quốc bắt đầu làm rung chuyển chính giới Pháp!',
                action: 'ambient'
            },
            {
                id: 'act4_2',
                image: 'act4_2_paris_room.jpg',
                act: 'HỒI 4 • TỎA SÁNG CHÂN LÝ',
                actIndex: 4,
                sceneNum: 'Cảnh 2/4',
                location: 'Ngõ Compoint, Quận 17, Paris',
                coords: 'Paris (Pháp) • Tháng 7/1920 (Mùa Hè)',
                speaker: 'Người Dẫn Truyện',
                role: 'Căn phòng trọ nghèo ngõ Compoint',
                text: 'Trong căn gác trọ nhỏ mùa đông sưởi bằng viên gạch nung bọc báo, tháng 7 năm 1920, Bác ngồi bên chiếc bàn gỗ đọc "Sơ thảo lần thứ nhất những luận cương về vấn đề dân tộc và thuộc địa" của V.I. Lênin đăng trên báo L’Humanité.',
                action: 'ambient'
            },
            {
                id: 'act4_2_quote',
                image: 'act4_2_paris_room.jpg',
                act: 'HỒI 4 • TỎA SÁNG CHÂN LÝ',
                actIndex: 4,
                sceneNum: 'Cảnh 3/4',
                location: 'Ngõ Compoint, Quận 17, Paris',
                coords: 'Paris (Pháp) • Tháng 7/1920',
                speaker: 'Nguyễn Ái Quốc',
                role: 'Reo to lên một mình trong phòng trọ như nói với toàn thể đồng bào',
                text: 'Hỡi đồng bào bị đọa đày đau khổ! Đây là cái cần thiết cho chúng ta, đây là con đường giải phóng chúng ta! Luận cương của Lênin làm cho tôi rất cảm động, phấn khởi, sáng tỏ, tin tưởng biết bao! Muốn cứu nước và giải phóng dân tộc không có con đường nào khác con đường cách mạng vô sản!',
                action: 'ambient'
            },
            {
                id: 'act4_3',
                image: 'act4_3_tours_congress.jpg',
                act: 'HỒI 4 • TỎA SÁNG CHÂN LÝ',
                actIndex: 4,
                sceneNum: 'Cảnh 4/4',
                location: 'Đại Hội Lần Thứ 18 Đảng Xã Hội Pháp (Tours)',
                coords: 'Tours (Pháp) • Tháng 12/1920 & Báo Le Paria 1922',
                speaker: 'Người Dẫn Truyện',
                role: 'Người cộng sản Việt Nam đầu tiên',
                text: 'Tháng 12/1920 tại Đại hội Tours, Người bỏ phiếu tán thành Quốc tế Cộng sản, tham gia sáng lập Đảng Cộng sản Pháp. Năm 1922, Người sáng lập báo Le Paria (Người Cùng Khổ) — ngọn cờ tập hợp các dân tộc thuộc địa trên toàn thế giới đứng lên đấu tranh tự giải phóng mình.',
                action: 'ambient'
            },

            // === HỒI 5: NGỌN LỬA LAN TỎA CÁCH MẠNG (1923 – 1930) ===
            {
                id: 'act5_1',
                image: 'act5_1_moscow_1923.jpg',
                act: 'HỒI 5 • NGỌN LỬA LAN TỎA',
                actIndex: 5,
                sceneNum: 'Cảnh 1/4',
                location: 'Mát-xcơ-va (Liên Xô) • 1923 – 1924',
                coords: 'Đại Học Phương Đông (KUTV), Mát-xcơ-va',
                speaker: 'Người Dẫn Truyện',
                role: 'Quê hương của Cách mạng Tháng Mười',
                text: 'Mùa đông 1923, vượt qua sự truy lùng gắt gao của mật thám Pháp, Người bí mật sang Mát-xcơ-va. Tại Đại học Phương Đông và Đại hội V Quốc tế Cộng sản, Người khẳng định vai trò quyết định của phong trào giải phóng dân tộc ở các nước thuộc địa đối với cách mạng thế giới.',
                action: 'ambient'
            },
            {
                id: 'act5_2',
                image: 'act5_2_guangzhou_school.jpg',
                act: 'HỒI 5 • NGỌN LỬA LAN TỎA',
                actIndex: 5,
                sceneNum: 'Cảnh 2/4',
                location: 'Nhà Số 13 Đường Văn Minh, Quảng Châu',
                coords: 'Quảng Châu (Trung Quốc) • Năm 1925 – 1927',
                speaker: 'Người Dẫn Truyện',
                role: 'Lớp huấn luyện cán bộ cách mạng thanh niên',
                text: 'Cuối năm 1924, Người về Quảng Châu mang bí danh Lý Thụy, thành lập Hội Việt Nam Cách mạng Thanh niên. Năm 1927, Người xuất bản tác phẩm kinh điển "Đường Kách Mệnh": "Cách mệnh trước hết phải có cái gì? Trước hết phải có Đảng cách mệnh..." — kim chỉ nam đào tạo lớp chiến sĩ cách mạng tiền phong.',
                action: 'ambient'
            },
            {
                id: 'act5_3',
                image: 'act5_3_hongkong_unification.jpg',
                act: 'HỒI 5 • NGỌN LỬA LAN TỎA',
                actIndex: 5,
                sceneNum: 'Cảnh 3/4',
                location: 'Cửu Long, Hương Cảng (Hong Kong)',
                coords: 'Hương Cảng • Mùa Xuân Ngày 03.02.1930',
                speaker: 'Nguyễn Ái Quốc',
                role: 'Chủ trì Hội nghị hợp nhất Đảng',
                text: 'Các đồng chí! Đều là những người cộng sản cùng chung mục đích cứu nước, tại sao lại chia rẽ làm ba tổ chức? Hãy gạt bỏ mọi bất đồng cục bộ, đoàn kết lại thành một Đảng duy nhất để lãnh đạo toàn dân làm cách mạng!',
                action: 'diegetic_unification'
            },
            {
                id: 'act5_3_summary',
                image: 'act5_3_hongkong_unification.jpg',
                act: 'HỒI 5 • NGỌN LỬA LAN TỎA',
                actIndex: 5,
                sceneNum: 'Cảnh 4/4',
                location: 'Cửu Long, Hương Cảng',
                coords: 'Ngày 03.02.1930 • Bước Ngoặt Vĩ Đại',
                speaker: 'Người Dẫn Truyện',
                role: 'Đảng Cộng sản Việt Nam ra đời',
                text: 'Hội nghị nhất trí hợp nhất các tổ chức thành Đảng Cộng sản Việt Nam, thông qua Chánh cương vắn tắt, Sách lược vắn tắt do Nguyễn Ái Quốc khởi thảo. Cuộc khủng hoảng đường lối cứu nước kéo dài gần nửa thế kỷ đã chính thức chấm dứt!',
                action: 'ambient'
            },

            // === HỒI 6: MÙA XUÂN TRỞ VỀ & BÌNH MINH NON SÔNG (1941) ===
            {
                id: 'act6_1',
                image: 'act5_1_pacbo_return.jpg',
                act: 'HỒI 6 • MÙA XUÂN TRỞ VỀ',
                actIndex: 6,
                sceneNum: 'Cảnh 1/3',
                location: 'Cột Mốc 108 Biên Giới Việt - Trung',
                coords: 'Pác Bó, Hà Quảng, Cao Bằng • 28.01.1941',
                speaker: 'Người Dẫn Truyện',
                role: 'Cột mốc 108 Cao Bằng (Sau 30 năm bôn ba)',
                text: 'Ngày 28 tháng 1 năm 1941 — sau tròn 30 năm bôn ba khắp năm châu bốn biển, Bác Hồ kính yêu đặt bước chân thiêng liêng đầu tiên trở về đất mẹ qua cột mốc 108 Cao Bằng. Hãy nhấp chạm vào Cột mốc biên giới để cảm nhận hơi ấm quê hương sau ba thập kỷ chia xa!',
                action: 'diegetic_milestone'
            },
            {
                id: 'act6_2',
                image: 'act5_2_pacbo_lamp.jpg',
                act: 'HỒI 6 • MÙA XUÂN TRỞ VỀ',
                actIndex: 6,
                sceneNum: 'Cảnh 2/3',
                location: 'Hang Cốc Bó, Suối Lênin',
                coords: 'Pác Bó, Cao Bằng • Mùa Xuân 1941',
                speaker: 'Người Dẫn Truyện',
                role: 'Bàn đá chông chênh hang Pác Bó',
                text: '"Bàn đá chông chênh dịch sử Đảng / Cuộc đời cách mạng thật là sang". Bên dòng suối Lênin xanh biếc, chiếc đèn dầu mộc mạc lại thắp sáng trong hang đá, soi đường cho Hội nghị Trung ương 8 quyết định thành lập Mặt trận Việt Minh, giương cao ngọn cờ giải phóng dân tộc, chuẩn bị cho ngày Tổng khởi nghĩa.',
                action: 'ambient'
            },
            {
                id: 'act6_3',
                image: 'act5_3_sunrise_independence.jpg',
                act: 'HỒI 6 • BÌNH MINH ĐỘC LẬP',
                actIndex: 6,
                sceneNum: 'Cảnh 3/3',
                location: 'Việt Nam • Độc Lập - Tự Do - Hạnh Phúc',
                coords: 'Quảng Trường Ba Đình • Mùa Thu Lịch Sử',
                speaker: 'Người Dẫn Truyện',
                role: 'Bình minh Độc Lập • Đúc kết Tư tưởng Hồ Chí Minh',
                text: 'Từ ngọn đèn dầu nhỏ nhoi trong căn gác trọ Sài Gòn năm 1911, ngọn lửa yêu nước và ý chí bất khuất đã bùng lên thành Ánh Bình Minh Độc Lập chói lọi! "Không có gì quý hơn độc lập, tự do!" — Tư tưởng Hồ Chí Minh mãi mãi là ngọn hải đăng soi sáng non sông Việt Nam.',
                action: 'diegetic_dawn'
            }
        ];

        /* ----------------------------------------------------
         * 2. STATE MANAGEMENT
         * ---------------------------------------------------- */
        function toggleHideUI() {
            state.isUIHidden = !state.isUIHidden;
            const elements = document.querySelectorAll('.hud-element');
            elements.forEach(el => {
                if (state.isUIHidden) {
                    el.classList.add('opacity-0', 'pointer-events-none');
                } else {
                    el.classList.remove('opacity-0', 'pointer-events-none');
                }
            });
            const openIco = document.getElementById('iconEyeOpen');
            const closeIco = document.getElementById('iconEyeClosed');
            if (openIco) openIco.classList.toggle('hidden', state.isUIHidden);
            if (closeIco) closeIco.classList.toggle('hidden', !state.isUIHidden);
        }

        let state = {
            isUIHidden: false,
            currentStepIndex: 0,
            activeBgLayer: 'A',
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
            prologueActive: true,
            prologueIndex: 0,
            boilerShovelsCount: 0,
            boilerCoalsCount: 0,
            wordsLearnedCount: 0,
            marseilleExplored: { left: false, right: false },
            marseilleSpatialView: 'center',
            marseilleDiscoveriesCount: 0,
            badgesUnified: 0,
            playerName: 'Nguyễn Văn Đồng Hành',
            playerAge: 21
        };

        /* ----------------------------------------------------
         * 3. PROCEDURAL WEB AUDIO SYNTHESIZERS
         * ---------------------------------------------------- */
        let audioCtx = null;

        function initAudioContext() {
            if (!audioCtx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                audioCtx = new AudioContext();
            }
            if (audioCtx.state === 'suspended') audioCtx.resume();
        }

        function playShipHorn(customGain = 0.28) {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            const freqs = [108, 136.5, 216];
            const hornGain = audioCtx.createGain();
            hornGain.gain.setValueAtTime(0.001, t);
            hornGain.gain.exponentialRampToValueAtTime(customGain, t + 0.5);
            hornGain.gain.exponentialRampToValueAtTime(0.0001, t + 4.0);

            freqs.forEach(f => {
                const osc = audioCtx.createOscillator();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(f, t);
                const filter = audioCtx.createBiquadFilter();
                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(450, t);
                osc.connect(filter);
                filter.connect(hornGain);
                osc.start(t);
                osc.stop(t + 4.0);
            });
            hornGain.connect(audioCtx.destination);
        }

        function playShovelScrapeSound() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            const bSize = audioCtx.sampleRate * 0.4;
            const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;
            const src = audioCtx.createBufferSource();
            src.buffer = buffer;
            const filter = audioCtx.createBiquadFilter();
            filter.type = 'bandpass';
            filter.frequency.setValueAtTime(1200, t);
            filter.Q.setValueAtTime(3.0, t);
            const gain = audioCtx.createGain();
            gain.gain.setValueAtTime(0.001, t);
            gain.gain.exponentialRampToValueAtTime(0.18, t + 0.05);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.38);
            src.connect(filter);
            filter.connect(gain);
            gain.connect(audioCtx.destination);
            src.start(t);
        }

        function playSteamReleaseSound() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            const bSize = audioCtx.sampleRate * 1.8;
            const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;
            const src = audioCtx.createBufferSource();
            src.buffer = buffer;
            const filter = audioCtx.createBiquadFilter();
            filter.type = 'highpass';
            filter.frequency.setValueAtTime(800, t);
            const gain = audioCtx.createGain();
            gain.gain.setValueAtTime(0.001, t);
            gain.gain.exponentialRampToValueAtTime(0.22, t + 0.2);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 1.8);
            src.connect(filter);
            filter.connect(gain);
            gain.connect(audioCtx.destination);
            src.start(t);
        }

        function playGaugeTickSound() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(980, t);
            osc.frequency.exponentialRampToValueAtTime(400, t + 0.08);
            gain.gain.setValueAtTime(0.15, t);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.08);
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.start(t);
            osc.stop(t + 0.08);
        }

        function playFurnaceSound() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;

            // Roaring whoosh
            const bSize = audioCtx.sampleRate * 1.5;
            const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;

            const src = audioCtx.createBufferSource();
            src.buffer = buffer;
            const filter = audioCtx.createBiquadFilter();
            filter.type = 'bandpass';
            filter.frequency.setValueAtTime(360, t);
            filter.Q.setValueAtTime(1.8, t);

            const nGain = audioCtx.createGain();
            nGain.gain.setValueAtTime(0.001, t);
            nGain.gain.exponentialRampToValueAtTime(0.35, t + 0.25);
            nGain.gain.exponentialRampToValueAtTime(0.001, t + 1.5);

            src.connect(filter);
            filter.connect(nGain);
            nGain.connect(audioCtx.destination);
            src.start(t);
        }

        function playPencilScratchSound() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            for (let stroke = 0; stroke < 2; stroke++) {
                const strokeTime = t + stroke * 0.11;
                const bSize = Math.floor(audioCtx.sampleRate * 0.085);
                const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
                const data = buffer.getChannelData(0);
                for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;

                const src = audioCtx.createBufferSource();
                src.buffer = buffer;
                const filter = audioCtx.createBiquadFilter();
                filter.type = 'bandpass';
                filter.frequency.setValueAtTime(2600 + (stroke * 350), strokeTime);
                filter.Q.setValueAtTime(2.6, strokeTime);

                const gain = audioCtx.createGain();
                gain.gain.setValueAtTime(0.001, strokeTime);
                gain.gain.linearRampToValueAtTime(0.14, strokeTime + 0.015);
                gain.gain.exponentialRampToValueAtTime(0.001, strokeTime + 0.08);

                src.connect(filter);
                filter.connect(gain);
                gain.connect(audioCtx.destination);
                src.start(strokeTime);
            }
        }

        function playStampSound() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            const osc = audioCtx.createOscillator();
            const oscGain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(115, t);
            osc.frequency.exponentialRampToValueAtTime(32, t + 0.14);

            oscGain.gain.setValueAtTime(0.35, t);
            oscGain.gain.exponentialRampToValueAtTime(0.001, t + 0.22);
            osc.connect(oscGain);
            oscGain.connect(audioCtx.destination);
            osc.start(t);
            osc.stop(t + 0.22);
        }

        function playPledgeChime() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            [220, 330, 440, 660].forEach(f => {
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

        function playMarseilleDiscoverySound() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            [523.25, 659.25, 783.99, 1046.50].forEach((f, idx) => {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(f, t + idx * 0.05);
                gain.gain.setValueAtTime(0.001, t + idx * 0.05);
                gain.gain.exponentialRampToValueAtTime(0.12 / (idx + 1), t + idx * 0.05 + 0.04);
                gain.gain.exponentialRampToValueAtTime(0.0001, t + 3.2);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start(t + idx * 0.05);
                osc.stop(t + 3.3);
            });
        }

        function playMarseilleWhipSound() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            const bSize = Math.floor(audioCtx.sampleRate * 0.35);
            const buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bSize; i++) data[i] = Math.random() * 2 - 1;
            const src = audioCtx.createBufferSource();
            src.buffer = buffer;
            const filter = audioCtx.createBiquadFilter();
            filter.type = 'lowpass';
            filter.frequency.setValueAtTime(600, t);
            filter.frequency.exponentialRampToValueAtTime(1500, t + 0.12);
            filter.frequency.exponentialRampToValueAtTime(300, t + 0.32);
            const gain = audioCtx.createGain();
            gain.gain.setValueAtTime(0.001, t);
            gain.gain.linearRampToValueAtTime(0.18, t + 0.08);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.34);
            src.connect(filter);
            filter.connect(gain);
            gain.connect(audioCtx.destination);
            src.start(t);
        }

        function playStoneChime() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            [216, 432, 648].forEach((f, idx) => {
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

        function playDawnBloomChord() {
            initAudioContext();
            if (!audioCtx || !state.audioEnabled) return;
            const t = audioCtx.currentTime;
            [261.63, 392.00, 523.25, 659.25, 783.99, 1046.50].forEach((f, idx) => {
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

        function playTypewriterKey() {
            if (!audioCtx || !state.audioEnabled) return;
            try {
                const t = audioCtx.currentTime;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(1800 + Math.random() * 600, t);
                gain.gain.setValueAtTime(0.02, t);
                gain.gain.exponentialRampToValueAtTime(0.0001, t + 0.035);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start(t);
                osc.stop(t + 0.035);
            } catch (e) {}
        }

        /* ----------------------------------------------------
         * 4. PROLOGUE LOGIC
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
                buttonText: 'BẮT ĐẦU HẢI TRÌNH 30 NĂM →'
            }
        ];

        function renderPrologueSlide() {
            const slide = PROLOGUE_SLIDES[state.prologueIndex];
            if (!slide) return;

            const bgImg = document.getElementById('prologueBgImg');
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
            stopPrologueSoundtrack();

            const pStage = document.getElementById('prologueStage');
            pStage.classList.add('opacity-0', 'pointer-events-none');
            playPledgeChime();

            setTimeout(() => {
                pStage.classList.add('hidden');
                state.currentStepIndex = 0;
                renderCurrentStep();
            }, 800);
        }

        function skipPrologue() { finishPrologue(); }

        let prologueMusic = null;
        function startPrologueSoundtrack() {
            initAudioContext();
            if (!state.audioEnabled) return;
            const audioEl = document.getElementById('prologueBgmAudio');
            if (audioEl && audioEl.paused) {
                audioEl.volume = 0.45;
                audioEl.play().catch(e => {});
            }
        }

        function stopPrologueSoundtrack() {
            const audioEl = document.getElementById('prologueBgmAudio');
            if (audioEl && !audioEl.paused) {
                audioEl.pause();
                audioEl.currentTime = 0;
            }
        }

        /* ----------------------------------------------------
         * 5. DIEGETIC IN-SCENE INTERACTION HANDLERS (NO POPUPS!)
         * ---------------------------------------------------- */
        
        // 5.1. Tiếp Than Hầm Tàu 40°C: Modal Cận Cảnh Đốt Lò Hơi (Close-Up Workshop v2 - Kéo Thả Trực Tiếp Cục Than)
        let activeDraggedCoalIndex = null;
        let isDraggingCoal = false;
        let coalDragOffset = { x: 0, y: 0 };
        let draggedCoalEl = null;

        function openBoilerModal() {
            initAudioContext();
            state.boilerCoalsCount = 0;
            state.boilerShovelsCount = 0;

            // Reset coal chunks in trough
            for (let i = 1; i <= 3; i++) {
                const el = document.getElementById(`coalChunk${i}`);
                if (el) {
                    el.classList.remove('opacity-0', 'scale-0', 'pointer-events-none');
                    el.style.position = '';
                    el.style.left = '';
                    el.style.top = '';
                    el.style.transform = '';
                    el.style.zIndex = '';
                }
            }

            const instText = document.getElementById('modalInstructionText');
            if (instText) instText.innerHTML = 'Kéo từng cục than đá antraxit bên dưới (hoặc bấm chọn) ném vào ngọn lửa rực hồng để giữ áp suất cho con tàu!';
            const hintText = document.getElementById('modalFooterHint');
            if (hintText) hintText.textContent = 'Hướng dẫn: Kéo từng cục than thả vào cửa lò, hoặc nhấp thẳng vào cục than để ném vào ngọn lửa!';

            updateModalBoilerUI();
            document.getElementById('boilerWorkshopModal').classList.remove('hidden');
        }

        function closeBoilerModal() {
            document.getElementById('boilerWorkshopModal').classList.add('hidden');
        }

        function updateModalBoilerUI() {
            const needle = document.getElementById('modalGaugeNeedle');
            const valText = document.getElementById('modalGaugeValue');
            const bar = document.getElementById('modalPressureBar');
            const counter = document.getElementById('modalStokeCounter');

            const angles = [-45, -5, 30, 75];
            const percents = [35, 60, 85, 100];
            const labels = ['35% (Mức Thấp)', '60% (Đang Tăng)', '85% (Áp Suất Cao)', '100% TỐI ĐA (ĐỦ ÁP SUẤT)'];

            const idx = Math.min(state.boilerCoalsCount || 0, 3);
            if (needle) needle.style.transform = `rotate(${angles[idx]}deg)`;
            if (bar) bar.style.width = `${percents[idx]}%`;
            if (valText) valText.textContent = `Áp Suất: ${labels[idx]}`;
            if (counter) counter.textContent = `${idx} / 3 Cục Than`;
        }

        function tossCoalChunk(num) {
            initAudioContext();
            const coalEl = document.getElementById(`coalChunk${num}`);
            if (!coalEl || coalEl.classList.contains('pointer-events-none')) return;

            const targetEl = document.getElementById('modalFurnaceTarget');
            if (targetEl) {
                const coalRect = coalEl.getBoundingClientRect();
                const targetRect = targetEl.getBoundingClientRect();

                // Fly animation
                coalEl.style.transition = 'all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1)';
                const deltaX = (targetRect.left + targetRect.width / 2) - (coalRect.left + coalRect.width / 2);
                const deltaY = (targetRect.top + targetRect.height / 2) - (coalRect.top + coalRect.height / 2);
                coalEl.style.transform = `translate(${deltaX}px, ${deltaY}px) scale(0.3) rotate(180deg)`;
                coalEl.style.opacity = '0.7';

                setTimeout(() => {
                    burnCoalChunk(num, targetRect.left + targetRect.width / 2, targetRect.top + targetRect.height / 2);
                }, 400);
            } else {
                burnCoalChunk(num);
            }
        }

        function startDragCoal(e, num) {
            initAudioContext();
            const coalEl = document.getElementById(`coalChunk${num}`);
            if (!coalEl || coalEl.classList.contains('pointer-events-none')) return;

            isDraggingCoal = true;
            activeDraggedCoalIndex = num;
            draggedCoalEl = coalEl;
            coalEl.setPointerCapture(e.pointerId);

            const rect = coalEl.getBoundingClientRect();
            coalDragOffset.x = e.clientX - rect.left;
            coalDragOffset.y = e.clientY - rect.top;
        }

        window.addEventListener('pointermove', (e) => {
            if (!isDraggingCoal || !draggedCoalEl) return;
            const newX = e.clientX - coalDragOffset.x;
            const newY = e.clientY - coalDragOffset.y;
            draggedCoalEl.style.position = 'fixed';
            draggedCoalEl.style.left = `${newX}px`;
            draggedCoalEl.style.top = `${newY}px`;
            draggedCoalEl.style.zIndex = '100';

            const fTarget = document.getElementById('modalFurnaceTarget');
            if (!fTarget) return;
            const fRect = fTarget.getBoundingClientRect();
            const cRect = draggedCoalEl.getBoundingClientRect();

            const isOver = (
                cRect.right >= fRect.left &&
                cRect.left <= fRect.right &&
                cRect.bottom >= fRect.top &&
                cRect.top <= fRect.bottom
            );

            if (isOver) {
                fTarget.classList.add('border-amber-300', 'bg-red-900/40', 'scale-102');
            } else {
                fTarget.classList.remove('border-amber-300', 'bg-red-900/40', 'scale-102');
            }
        });

        window.addEventListener('pointerup', (e) => {
            if (!isDraggingCoal || !draggedCoalEl) return;
            const coalIdx = activeDraggedCoalIndex;
            const coalEl = draggedCoalEl;
            isDraggingCoal = false;
            activeDraggedCoalIndex = null;
            draggedCoalEl = null;

            const fTarget = document.getElementById('modalFurnaceTarget');
            if (fTarget) fTarget.classList.remove('border-amber-300', 'bg-red-900/40', 'scale-102');

            if (fTarget) {
                const fRect = fTarget.getBoundingClientRect();
                const cRect = coalEl.getBoundingClientRect();
                const isOver = (
                    cRect.right >= fRect.left &&
                    cRect.left <= fRect.right &&
                    cRect.bottom >= fRect.top &&
                    cRect.top <= fRect.bottom
                );

                if (isOver) {
                    burnCoalChunk(coalIdx, e.clientX, e.clientY);
                    return;
                }
            }

            // If not dropped in fire, snap back
            coalEl.style.position = '';
            coalEl.style.left = '';
            coalEl.style.top = '';
            coalEl.style.zIndex = '';
        });

        function burnCoalChunk(num, dropX, dropY) {
            const coalEl = document.getElementById(`coalChunk${num}`);
            if (coalEl) {
                coalEl.classList.add('opacity-0', 'scale-0', 'pointer-events-none');
                coalEl.style.position = '';
                coalEl.style.left = '';
                coalEl.style.top = '';
                coalEl.style.transform = '';
                coalEl.style.zIndex = '';
            }

            state.boilerCoalsCount = (state.boilerCoalsCount || 0) + 1;
            state.boilerShovelsCount = state.boilerCoalsCount;

            playFurnaceSound();
            playSteamReleaseSound();
            playGaugeTickSound();

            // Screen shake inside modal
            const modalBox = document.getElementById('boilerWorkshopModal');
            if (modalBox) {
                modalBox.classList.remove('animate-rumble');
                void modalBox.offsetWidth;
                modalBox.classList.add('animate-rumble');
            }

            // Emit sparks from drop point or center of furnace
            const fTarget = document.getElementById('modalFurnaceTarget');
            let sparkX = dropX;
            let sparkY = dropY;
            if ((!sparkX || !sparkY) && fTarget) {
                const rect = fTarget.getBoundingClientRect();
                sparkX = rect.left + rect.width / 2;
                sparkY = rect.top + rect.height / 2;
            }
            if (sparkX && sparkY) {
                emitSparks(sparkX, sparkY, 25);
            }

            updateModalBoilerUI();
            state.resonance = Math.min(100, state.resonance + 15);
            updateResonanceHUD();

            if (state.boilerCoalsCount >= 3) {
                playShipHorn(0.5);
                const instText = document.getElementById('modalInstructionText');
                const hintText = document.getElementById('modalFooterHint');
                if (instText) instText.innerHTML = '<span class="text-emerald-400 font-bold">HOÀN THÀNH: NỒI HƠI ĐẠT ĐỈNH 100% ÁP SUẤT!</span>';
                if (hintText) hintText.textContent = 'Con tàu Amiral Latouche-Tréville tăng tốc rẽ sóng ra khơi! Tự động chuyển cảnh...';

                setTimeout(() => {
                    closeBoilerModal();
                    const hotspot = document.getElementById('furnaceHotspot');
                    if (hotspot) hotspot.classList.add('hidden');
                    const targetIdx = SCENE_SCRIPT.findIndex(s => s.id === 'ship_1_dialogue');
                    state.currentStepIndex = targetIdx !== -1 ? targetIdx : 8;
                    renderCurrentStep();
                }, 1600);
            }
        }

        // 5.2. Sổ Thuyền Viên Bến Cảng 1911 (Diegetic Register)
        function stampInsceneRegister() {
            playStampSound();
            const pName = document.getElementById('inscenePlayerName').value.trim() || 'Nguyễn Văn Đồng Hành';
            const pAge = document.getElementById('inscenePlayerAge').value.trim() || '21';
            state.playerName = pName;
            state.playerAge = pAge;

            const stampMark = document.getElementById('insceneStampMark');
            stampMark.classList.remove('hidden');

            state.resonance = Math.min(100, state.resonance + 20);
            updateResonanceHUD();

            state.historyLog.push({
                speaker: 'Thủ Tục Lịch Sử',
                role: 'Sổ Thuyền Viên Chargeurs Réunis 1911',
                text: `Ký tên trên bến cảng: ${pName} (${pAge} tuổi) — Chức vụ: Aide-cuisinier (Phụ Bếp) cùng anh Văn Ba.`
            });

            setTimeout(() => {
                document.getElementById('diegeticRegisterRig').classList.add('hidden');
                stampMark.classList.add('hidden');
                const targetIdx = SCENE_SCRIPT.findIndex(s => s.id === 'dock_3');
                state.currentStepIndex = targetIdx !== -1 ? targetIdx : 6;
                renderCurrentStep();
            }, 1600);
        }

        // 5.25. Học Từ Mới Dưới Ánh Đèn Dầu 1911 (Diegetic French Vocabulary Study)
        function learnWord(num, french, viet, insight) {
            initAudioContext();
            playPencilScratchSound();

            const writtenEl = document.getElementById(`writtenWord${num}`);
            const btnEl = document.getElementById(`btnStudyWord${num}`);
            const statusEl = document.getElementById(`studyWordStatus${num}`);
            const emptyPrompt = document.getElementById('notebookEmptyPrompt');
            const insightText = document.getElementById('studyAnhBaInsight');
            const counterBadge = document.getElementById('studyCounterBadge');

            if (emptyPrompt) emptyPrompt.classList.add('hidden');
            if (writtenEl && writtenEl.classList.contains('hidden')) {
                writtenEl.classList.remove('hidden');
                state.wordsLearnedCount = (state.wordsLearnedCount || 0) + 1;
            }

            if (btnEl) {
                btnEl.classList.remove('border-amber-500/50', 'bg-black/60');
                btnEl.classList.add('border-emerald-500/70', 'bg-emerald-950/40');
            }
            if (statusEl) {
                statusEl.className = 'text-[10px] font-typewriter px-2 py-0.5 rounded bg-emerald-500/30 text-emerald-300 border border-emerald-500/50 font-bold';
                statusEl.textContent = '✓ Đã ghi chép';
            }

            if (insightText) {
                insightText.textContent = `"${insight}"`;
            }

            if (counterBadge) {
                counterBadge.textContent = `${state.wordsLearnedCount} / 5 Từ Vựng`;
            }

            state.resonance = Math.min(100, state.resonance + 5);
            updateResonanceHUD();

            if (state.wordsLearnedCount >= 5) {
                playPledgeChime();
                const completionBox = document.getElementById('studyCompletionBox');
                if (completionBox) completionBox.classList.remove('hidden');
                if (insightText) {
                    insightText.innerHTML = '<strong class="text-amber-300">Anh Ba mỉm cười gật đầu:</strong> "Tốt lắm! Có tri thức là có tự do. Giờ hãy nghỉ ngơi một chút, rạng sáng mai chúng ta lại tiếp tục công việc!"';
                }
            }
        }

        function finishStudyScene() {
            initAudioContext();
            playShipHorn(0.35);

            state.historyLog.push({
                speaker: 'Góc Cabin Thuyền Viên 1911',
                role: 'Anh Ba & Bạn đồng hành',
                text: 'Dưới ánh đèn dầu bão leo lét giữa biển đêm, bạn và anh Ba cùng nhau học 5 từ vựng tiếng Pháp: La Liberté, L\'Égalité, La Fraternité, La Patrie, Le Peuple.'
            });

            const studyRig = document.getElementById('diegeticStudyRig');
            if (studyRig) studyRig.classList.add('hidden');

            state.resonance = Math.min(100, state.resonance + 15);
            updateResonanceHUD();

            const targetIdx = SCENE_SCRIPT.findIndex(s => s.id === 'marseille_step_1');
            state.currentStepIndex = targetIdx !== -1 ? targetIdx : 9;
            renderCurrentStep();
        }

        function resetStudyUI() {
            state.wordsLearnedCount = 0;
            const emptyPrompt = document.getElementById('notebookEmptyPrompt');
            if (emptyPrompt) emptyPrompt.classList.remove('hidden');

            for (let i = 1; i <= 5; i++) {
                const w = document.getElementById(`writtenWord${i}`);
                if (w) w.classList.add('hidden');
                const b = document.getElementById(`btnStudyWord${i}`);
                if (b) {
                    b.classList.remove('border-emerald-500/70', 'bg-emerald-950/40');
                    b.classList.add('border-amber-500/50', 'bg-black/60');
                }
                const s = document.getElementById(`studyWordStatus${i}`);
                if (s) {
                    s.className = 'text-[10px] font-typewriter px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30';
                    s.textContent = 'Học từ này →';
                }
            }
            const cBox = document.getElementById('studyCompletionBox');
            if (cBox) cBox.classList.add('hidden');
            const cBadge = document.getElementById('studyCounterBadge');
            if (cBadge) cBadge.textContent = '0 / 5 Từ Vựng';
            const insightText = document.getElementById('studyAnhBaInsight');
            if (insightText) {
                insightText.textContent = '"Mỗi tối tôi tranh thủ học vài từ. Viết lên tay, viết lên sàn tàu để nhớ. Muốn đánh đổ xiềng xích, trước hết phải hiểu rõ kẻ thù!"';
            }
        }

        // 5.26. Cảng Marseille 1911: Điều Hướng Không Gian 3 Hướng & Chân Lý Lịch Sử
        function setStageBackgroundPlate(imageSrc, whipClass) {
            const activeLayer = state.activeBgLayer === 'A' ? document.getElementById('bgLayerA') : document.getElementById('bgLayerB');
            if (activeLayer) {
                activeLayer.classList.remove('marseille-whip-left', 'marseille-whip-right', 'marseille-whip-center');
                // Trigger reflow to restart animation cleanly
                void activeLayer.offsetWidth;
                activeLayer.src = imageSrc;
                if (whipClass) {
                    activeLayer.classList.add(whipClass);
                }
            }
        }

        function panToMarseilleView(direction) {
            initAudioContext();
            playMarseilleWhipSound();

            const centerNav = document.getElementById('marseilleCenterNav');
            const leftPanel = document.getElementById('marseilleLeftPanel');
            const rightPanel = document.getElementById('marseilleRightPanel');
            const epiphanyOverlay = document.getElementById('marseilleEpiphanyOverlay');
            const badge = document.getElementById('marseilleExplorationBadge');
            const leftStatus = document.getElementById('marseilleLeftStatus');
            const rightStatus = document.getElementById('marseilleRightStatus');
            const title = document.getElementById('marseilleSpatialTitle');
            const insightText = document.getElementById('marseilleInsightText');

            if (direction === 'left') {
                state.marseilleSpatialView = 'left';
                state.marseilleExplored.left = true;
                setStageBackgroundPlate('marseille_left_carts.jpg', 'marseille-whip-left');
                playMarseilleDiscoverySound();

                if (centerNav) centerNav.classList.add('hidden');
                if (leftPanel) leftPanel.classList.remove('hidden');
                if (rightPanel) rightPanel.classList.add('hidden');
                if (epiphanyOverlay) epiphanyOverlay.classList.add('hidden');

                if (title) title.textContent = 'Góc Trái: Phu Kéo Xe Da Trắng Bến Cảng';
                if (leftStatus) {
                    leftStatus.textContent = '✓ ĐÃ QUAN SÁT';
                    leftStatus.className = 'mt-2 text-[10px] font-typewriter px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-bold';
                }
                if (insightText) {
                    insightText.innerHTML = '<strong class="text-amber-300">Anh Ba chia sẻ:</strong> "Ngay tại chính quốc, người Pháp da trắng cũng phải kéo xe cực nhọc chẳng khác gì phu xe An Nam ta!"';
                }

                state.resonance = Math.min(100, state.resonance + 10);
                updateResonanceHUD();

            } else if (direction === 'right') {
                state.marseilleSpatialView = 'right';
                state.marseilleExplored.right = true;
                setStageBackgroundPlate('marseille_right_steps.jpg', 'marseille-whip-right');
                playMarseilleDiscoverySound();

                if (centerNav) centerNav.classList.add('hidden');
                if (leftPanel) leftPanel.classList.add('hidden');
                if (rightPanel) rightPanel.classList.remove('hidden');
                if (epiphanyOverlay) epiphanyOverlay.classList.add('hidden');

                if (title) title.textContent = 'Góc Phải: Bậc Đá Cảng Cũ & Người Cơ Hàn';
                if (rightStatus) {
                    rightStatus.textContent = '✓ ĐÃ QUAN SÁT';
                    rightStatus.className = 'mt-2 text-[10px] font-typewriter px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-bold';
                }
                if (insightText) {
                    insightText.innerHTML = '<strong class="text-amber-300">Anh Ba thoáng buồn:</strong> "Tại sao thực dân rêu rao sang khai hóa, trong khi trên đất nước họ người nghèo vẫn cơ hàn đói rách thế này?!"';
                }

                state.resonance = Math.min(100, state.resonance + 10);
                updateResonanceHUD();

            } else if (direction === 'center') {
                state.marseilleSpatialView = 'center';
                setStageBackgroundPlate('marseille_1_port.jpg', 'marseille-whip-center');

                if (leftPanel) leftPanel.classList.add('hidden');
                if (rightPanel) rightPanel.classList.add('hidden');

                if (title) title.textContent = 'Quảng Trường Cảng: Chọn Hướng Quan Sát Đời Sống';

                // Check if both directions have been explored
                if (state.marseilleExplored.left && state.marseilleExplored.right) {
                    if (centerNav) centerNav.classList.add('hidden');
                    showMarseilleEpiphany();
                } else {
                    if (centerNav) centerNav.classList.remove('hidden');
                    if (epiphanyOverlay) epiphanyOverlay.classList.add('hidden');
                }
            }

            const exploredCount = (state.marseilleExplored.left ? 1 : 0) + (state.marseilleExplored.right ? 1 : 0);
            if (badge) {
                badge.textContent = `${exploredCount} / 2 Hướng Khám Phá`;
                if (exploredCount >= 2) {
                    badge.className = 'px-3 py-1 rounded-full bg-emerald-950/80 border border-emerald-400 text-emerald-300 font-typewriter text-xs font-bold';
                }
            }
        }

        function showMarseilleEpiphany() {
            playPledgeChime();
            const epiphanyOverlay = document.getElementById('marseilleEpiphanyOverlay');
            if (epiphanyOverlay) epiphanyOverlay.classList.remove('hidden');

            state.resonance = 100;
            updateResonanceHUD();

            const insightText = document.getElementById('marseilleInsightText');
            if (insightText) {
                insightText.innerHTML = '<strong class="text-amber-300">Chân Lý Lịch Sử:</strong> "Kẻ thù là thực dân áp bức, còn nhân dân lao động Pháp chính là bạn bè!"';
            }
        }

        function finishMarseilleSpatialScene() {
            initAudioContext();
            playShipHorn(0.35);

            state.historyLog.push({
                speaker: 'Cảng Marseille • 06.07.1911',
                role: 'Nguyễn Tất Thành (Anh Ba)',
                text: 'Tại cảng Marseille, Bác đúc kết chân lý lớn đầu tiên: "Ở Pháp cũng có những người nghèo như ở xứ ta... Kẻ thù là ách áp bức thực dân, còn nhân dân lao động Pháp chính là bạn bè!"'
            });

            const marseilleRig = document.getElementById('diegeticMarseilleRig');
            if (marseilleRig) marseilleRig.classList.add('hidden');
            const epiphanyOverlay = document.getElementById('marseilleEpiphanyOverlay');
            if (epiphanyOverlay) epiphanyOverlay.classList.add('hidden');

            const targetIdx = SCENE_SCRIPT.findIndex(s => s.id === 'world_1');
            state.currentStepIndex = targetIdx !== -1 ? targetIdx : state.currentStepIndex + 1;
            renderCurrentStep();
        }

        function resetMarseilleSpatialUI() {
            state.marseilleExplored = { left: false, right: false };
            state.marseilleSpatialView = 'center';

            const centerNav = document.getElementById('marseilleCenterNav');
            const leftPanel = document.getElementById('marseilleLeftPanel');
            const rightPanel = document.getElementById('marseilleRightPanel');
            const epiphanyOverlay = document.getElementById('marseilleEpiphanyOverlay');
            const badge = document.getElementById('marseilleExplorationBadge');
            const leftStatus = document.getElementById('marseilleLeftStatus');
            const rightStatus = document.getElementById('marseilleRightStatus');
            const title = document.getElementById('marseilleSpatialTitle');

            if (centerNav) centerNav.classList.remove('hidden');
            if (leftPanel) leftPanel.classList.add('hidden');
            if (rightPanel) rightPanel.classList.add('hidden');
            if (epiphanyOverlay) epiphanyOverlay.classList.add('hidden');

            if (badge) {
                badge.textContent = '0 / 2 Hướng Khám Phá';
                badge.className = 'px-3 py-1 rounded-full bg-black/70 border border-sky-500/50 text-sky-300 font-typewriter text-xs font-bold';
            }
            if (leftStatus) {
                leftStatus.textContent = 'Chưa quan sát';
                leftStatus.className = 'mt-2 text-[10px] font-typewriter px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 border border-sky-500/30';
            }
            if (rightStatus) {
                rightStatus.textContent = 'Chưa quan sát';
                rightStatus.className = 'mt-2 text-[10px] font-typewriter px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 border border-sky-500/30';
            }
            if (title) title.textContent = 'Quảng Trường Cảng: Chọn Hướng Quan Sát Đời Sống';

            const insightText = document.getElementById('marseilleInsightText');
            if (insightText) {
                insightText.textContent = '"Người Pháp ở Pháp tốt và lịch sự hơn thực dân ở xứ ta rất nhiều..." — Văn Ba';
            }
        }

        // 5.3. Hợp Nhất 3 Tổ Chức Đảng (Diegetic Unification)
        function unifyBadge(num) {
            initAudioContext();
            playTypewriterKey();
            const btn = document.getElementById(`badge${num}`);
            btn.classList.add('bg-amber-600', 'text-black', 'scale-110');
            btn.disabled = true;
            state.badgesUnified++;

            if (state.badgesUnified >= 3) {
                playPledgeChime();
                document.getElementById('unifiedCrest').classList.remove('hidden');
                state.resonance = Math.min(100, state.resonance + 25);
                updateResonanceHUD();

                setTimeout(() => {
                    document.getElementById('diegeticUnificationRig').classList.add('hidden');
                    const targetIdx = SCENE_SCRIPT.findIndex(s => s.id === 'act5_3_summary');
                    state.currentStepIndex = targetIdx !== -1 ? targetIdx : state.currentStepIndex + 1;
                    renderCurrentStep();
                }, 1800);
            }
        }

        // 5.4. Chạm Cột Mốc 108 Pác Bó (Diegetic Milestone)
        function touchInsceneMilestone() {
            playStoneChime();
            const btn = document.getElementById('insceneMilestoneBtn');
            btn.classList.add('ring-4', 'ring-amber-400', 'scale-110');
            document.getElementById('inscenePoem').classList.remove('hidden');
            state.resonance = 100;
            updateResonanceHUD();

            setTimeout(() => {
                document.getElementById('diegeticMilestoneRig').classList.add('hidden');
                const targetIdx = SCENE_SCRIPT.findIndex(s => s.id === 'act6_2');
                state.currentStepIndex = targetIdx !== -1 ? targetIdx : state.currentStepIndex + 1;
                renderCurrentStep();
            }, 2400);
        }

        /* ----------------------------------------------------
         * 6. RENDER CURRENT STEP (STAGE DUAL CROSS-FADING ENGINE)
         * ---------------------------------------------------- */
        function renderCurrentStep() {
            const step = SCENE_SCRIPT[state.currentStepIndex];
            if (!step) return;

            // 1. HUD Updates
            document.getElementById('hudActBadge').textContent = step.act;
            document.getElementById('hudLocationTitle').textContent = step.location;
            document.getElementById('hudCoordinates').textContent = step.coords;
            document.getElementById('stepActSummary').textContent = `Hồi ${step.actIndex}/6:`;
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

            // 3. Smooth Dual Cross-Dissolve Stage Background
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

            // 4. Log text
            state.historyLog.push({ speaker: step.speaker, role: step.role, text: step.text });
            updateLogModalContent();

            // 5. Choices handling
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

            // 6. Diegetic In-Scene Activations
            handleDiegeticTriggers(step.action);

            // 7. Kinetic typewriter
            if (step.action === 'marseille_disembark_no_dialogue') {
                clearInterval(state.typingTimer);
                state.isTyping = false;
            } else {
                startTypewriter(step.text);
            }
        }

        function handleDiegeticTriggers(action) {
            const dialogueBox = document.getElementById('dialogueBox');
            const questBanner = document.getElementById('diegeticQuestBanner');
            const hotspot = document.getElementById('furnaceHotspot');
            const registerRig = document.getElementById('diegeticRegisterRig');
            const studyRig = document.getElementById('diegeticStudyRig');
            const marseilleRig = document.getElementById('diegeticMarseilleRig');
            const noDialogueCard = document.getElementById('marseilleNoDialogueCard');
            const unificationRig = document.getElementById('diegeticUnificationRig');
            const milestoneRig = document.getElementById('diegeticMilestoneRig');
            const dawnRig = document.getElementById('diegeticDawnRig');

            // Reset rigs and quest banner by default
            if (hotspot) hotspot.classList.add('hidden');
            if (registerRig) registerRig.classList.add('hidden');
            if (studyRig) studyRig.classList.add('hidden');
            if (marseilleRig) marseilleRig.classList.add('hidden');
            if (noDialogueCard) noDialogueCard.classList.add('hidden');
            if (unificationRig) unificationRig.classList.add('hidden');
            if (milestoneRig) milestoneRig.classList.add('hidden');
            if (dawnRig) dawnRig.classList.add('hidden');
            if (questBanner) questBanner.classList.add('hidden');

            // Restore dialogue box by default
            if (dialogueBox) dialogueBox.classList.remove('hidden');

            if (action === 'open_boiler_hotspot' || action === 'diegetic_boiler') {
                // Show pulsing hotspot on furnace door
                if (hotspot) hotspot.classList.remove('hidden');
            } else if (action === 'diegetic_register') {
                if (dialogueBox) dialogueBox.classList.add('hidden');
                if (questBanner) questBanner.classList.remove('hidden');
                const qTitle = document.getElementById('questTitle');
                if (qTitle) qTitle.textContent = 'THỦ TỤC XUẤT BẾN';
                const qSub = document.getElementById('questSubtitle');
                if (qSub) qSub.textContent = 'BẾN NHÀ RỒNG • 05/06/1911';
                const qInst = document.getElementById('questInstruction');
                if (qInst) qInst.textContent = 'Ký tên vào Sổ Thuyền Viên để nhận danh phận thủy thủ "Văn Ba" bước lên tàu';
                const qCount = document.getElementById('questCounter');
                if (qCount) qCount.textContent = 'Chờ ký tên';
                if (registerRig) registerRig.classList.remove('hidden');
            } else if (action === 'diegetic_study') {
                if (dialogueBox) dialogueBox.classList.add('hidden');
                if (studyRig) studyRig.classList.remove('hidden');
            } else if (action === 'marseille_disembark_no_dialogue') {
                if (dialogueBox) dialogueBox.classList.add('hidden');
                if (noDialogueCard) noDialogueCard.classList.remove('hidden');
                playShipHorn(0.3);
            } else if (action === 'diegetic_marseille_spatial') {
                if (dialogueBox) dialogueBox.classList.add('hidden');
                if (marseilleRig) marseilleRig.classList.remove('hidden');
                resetMarseilleSpatialUI();
            } else if (action === 'diegetic_unification') {
                if (dialogueBox) dialogueBox.classList.add('hidden');
                if (questBanner) questBanner.classList.remove('hidden');
                const qTitle = document.getElementById('questTitle');
                if (qTitle) qTitle.textContent = 'HỢP NHẤT LỊCH SỬ';
                const qSub = document.getElementById('questSubtitle');
                if (qSub) qSub.textContent = 'HƯƠNG CẢNG • 03/02/1930';
                const qInst = document.getElementById('questInstruction');
                if (qInst) qInst.textContent = 'Nhấp nút hợp nhất để hòa quyện 3 tổ chức thành một Đảng duy nhất';
                const qCount = document.getElementById('questCounter');
                if (qCount) qCount.textContent = 'Chờ hợp nhất';
                if (unificationRig) unificationRig.classList.remove('hidden');
            } else if (action === 'diegetic_milestone') {
                if (dialogueBox) dialogueBox.classList.add('hidden');
                if (questBanner) questBanner.classList.remove('hidden');
                const qTitle = document.getElementById('questTitle');
                if (qTitle) qTitle.textContent = 'MÙA XUÂN TRỞ VỀ';
                const qSub = document.getElementById('questSubtitle');
                if (qSub) qSub.textContent = 'CỘT MỐC 108 PÁC BÓ • 1941';
                const qInst = document.getElementById('questInstruction');
                if (qInst) qInst.textContent = 'Chạm tay vào Cột Mốc 108 để cảm nhận hơi ấm thiêng liêng của đất mẹ';
                const qCount = document.getElementById('questCounter');
                if (qCount) qCount.textContent = 'Chạm cột mốc';
                if (milestoneRig) milestoneRig.classList.remove('hidden');
            } else if (action === 'diegetic_dawn') {
                playDawnBloomChord();
                if (dawnRig) dawnRig.classList.remove('hidden');
            } else if (action === 'play_horn') {
                playShipHorn(0.35);
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

            if (state.autoPlay && !state.waitingForChoice) {
                clearTimeout(state.autoPlayTimer);
                state.autoPlayTimer = setTimeout(advanceDialogue, 4000);
            }
        }

        function advanceDialogue() {
            if (state.waitingForChoice) return;

            const currentStep = SCENE_SCRIPT[state.currentStepIndex];
            if (currentStep && currentStep.action === 'marseille_disembark_no_dialogue') {
                const targetIdx = SCENE_SCRIPT.findIndex(s => s.id === 'marseille_step_2');
                state.currentStepIndex = targetIdx !== -1 ? targetIdx : state.currentStepIndex + 1;
                renderCurrentStep();
                return;
            }

            if (state.isTyping) { finishTypewriter(); return; }

            if (currentStep && currentStep.action === 'open_boiler_hotspot') {
                openBoilerModal();
                return;
            }

            if (currentStep && currentStep.action === 'diegetic_study') {
                if (state.wordsLearnedCount >= 5) {
                    finishStudyScene();
                }
                return;
            }

            if (currentStep && currentStep.action === 'diegetic_marseille_spatial') {
                if (state.marseilleExplored && state.marseilleExplored.left && state.marseilleExplored.right) {
                    finishMarseilleSpatialScene();
                }
                return;
            }

            if (state.currentStepIndex < SCENE_SCRIPT.length - 1) {
                state.currentStepIndex++;
                renderCurrentStep();
            } else {
                document.getElementById('diegeticDawnRig').classList.remove('hidden');
            }
        }

        function renderChoices(choices) {
            const list = document.getElementById('choicesList');
            list.innerHTML = '';
            choices.forEach((c) => {
                const btn = document.createElement('button');
                btn.className = 'p-3.5 rounded-xl border border-brass/40 bg-abyss/90 hover:bg-brass/25 hover:border-brass text-left text-xs md:text-sm text-slate-100 transition-all flex items-start gap-2.5 cursor-pointer group';
                btn.onclick = (e) => {
                    e.stopPropagation();
                    selectChoice(c);
                };
                btn.innerHTML = `
                    <span class="inline-flex items-center justify-center min-w-[24px] h-6 rounded bg-brass/20 text-brass font-typewriter font-bold text-xs group-hover:bg-brass group-hover:text-void transition-colors">[${c.key}]</span>
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

        function handleDialogueBoxClick() { advanceDialogue(); }

        function updateResonanceHUD() {
            document.getElementById('resonanceScore').textContent = `${state.resonance}%`;
            document.getElementById('resonanceBar').style.width = `${state.resonance}%`;
        }

        /* ----------------------------------------------------
         * 7. TIME LENS, CHAPTER MENU & SHORTCUTS
         * ---------------------------------------------------- */
        function toggleTimeLens() {
            state.timeLensActive = !state.timeLensActive;
            playTypewriterKey();
        }

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
                if (typeof target === 'string') {
                    const idx = SCENE_SCRIPT.findIndex(s => s.id === target);
                    state.currentStepIndex = idx !== -1 ? idx : 0;
                } else {
                    state.currentStepIndex = target;
                }
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
            }
        }

        function toggleAutoPlay() {
            state.autoPlay = !state.autoPlay;
            const btn = document.getElementById('btnAutoPlay');
            if (state.autoPlay) {
                btn.classList.add('bg-brass', 'text-void');
                btn.classList.remove('bg-abyss/80', 'text-brass');
                if (!state.isTyping && !state.waitingForChoice) advanceDialogue();
            } else {
                btn.classList.remove('bg-brass', 'text-void');
                btn.classList.add('bg-abyss/80', 'text-brass');
                clearTimeout(state.autoPlayTimer);
            }
        }

        function restartExperience() {
            document.getElementById('diegeticDawnRig').classList.add('hidden');
            state.resonance = 25;
            state.boilerCoalsCount = 0;
            state.boilerShovelsCount = 0;
            state.wordsLearnedCount = 0;
            state.marseilleExplored = { left: false, right: false };
            state.marseilleSpatialView = 'center';
            state.badgesUnified = 0;
            resetStudyUI();
            resetMarseilleSpatialUI();
            updateResonanceHUD();
            openPrologue();
        }

        window.addEventListener('keydown', (e) => {
            // Do NOT capture keys when user is typing into an input field or textarea
            if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable)) {
                if (e.code === 'Enter') {
                    e.preventDefault();
                    if (e.target.id === 'inscenePlayerName' || e.target.id === 'inscenePlayerAge') {
                        stampInsceneRegister();
                    }
                }
                return;
            }

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

            // Marseille spatial navigation keyboard shortcuts
            const marseilleRig = document.getElementById('diegeticMarseilleRig');
            if (marseilleRig && !marseilleRig.classList.contains('hidden')) {
                if (e.key === 'ArrowLeft') {
                    e.preventDefault();
                    if (state.marseilleSpatialView === 'center' || state.marseilleSpatialView === 'right') {
                        panToMarseilleView('left');
                    }
                    return;
                } else if (e.key === 'ArrowRight') {
                    e.preventDefault();
                    if (state.marseilleSpatialView === 'center' || state.marseilleSpatialView === 'left') {
                        panToMarseilleView('right');
                    }
                    return;
                } else if (e.code === 'Escape' || e.code === 'Backspace') {
                    e.preventDefault();
                    if (state.marseilleSpatialView !== 'center') {
                        panToMarseilleView('center');
                    }
                    return;
                }
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
            } else if (e.key.toLowerCase() === 'c') {
                toggleChapterMenu(true);
            } else if (e.key.toLowerCase() === 'm') {
                toggleAudio();
            } else if (e.key.toLowerCase() === 'a') {
                toggleAutoPlay();
            } else if (e.key.toLowerCase() === 'l') {
                toggleLogModal(document.getElementById('logModal').classList.contains('hidden'));
            } else if (e.key.toLowerCase() === 'h') {
                toggleHideUI();
            } else if (e.key.toLowerCase() === 'r') {
                restartExperience();
            } else if (e.code === 'Escape') {
                toggleLogModal(false);
                toggleChapterMenu(false);
            }
        });

        /* ----------------------------------------------------
         * 8. CANVAS PARTICLES & SPARKS (60 FPS)
         * ---------------------------------------------------- */
        const canvas = document.getElementById('skyCanvas');
        const ctx = canvas ? canvas.getContext('2d') : null;
        let stars = [];

        function resizeCanvas() {
            if (!canvas) return;
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            stars = [];
            for (let i = 0; i < 80; i++) {
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

        // Sparks Canvas
        const sparkCanvas = document.getElementById('sparkCanvas');
        const sparkCtx = sparkCanvas ? sparkCanvas.getContext('2d') : null;
        let sparks = [];

        function resizeSparkCanvas() {
            if (!sparkCanvas) return;
            sparkCanvas.width = window.innerWidth;
            sparkCanvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeSparkCanvas);
        resizeSparkCanvas();

        function emitSparks(originX, originY, velocityX = 0) {
            for (let i = 0; i < 50; i++) {
                const angle = Math.random() * Math.PI - (Math.PI / 2);
                const speed = Math.random() * 9 + 3;
                sparks.push({
                    x: originX,
                    y: originY,
                    vx: Math.cos(angle) * speed + velocityX,
                    vy: Math.sin(angle) * speed - 3,
                    radius: Math.random() * 2.8 + 1.2,
                    alpha: 1,
                    color: Math.random() > 0.35 ? '#f59e0b' : '#fef08a'
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
                s.vy += 0.28;
                s.alpha -= 0.024;
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

        // Continuous Harbor Steam / Boiler Smoke
        const smokeCanvas = document.getElementById('smokeCanvas');
        const sCtx = smokeCanvas ? smokeCanvas.getContext('2d') : null;
        let smokeParticles = [];

        function resizeSmoke() {
            if (!smokeCanvas) return;
            smokeCanvas.width = window.innerWidth;
            smokeCanvas.height = window.innerHeight;
        }

        function emitSmoke() {
            if (smokeParticles.length < 24) {
                smokeParticles.push({
                    x: window.innerWidth * 0.6 + (Math.random() * 30 - 15),
                    y: window.innerHeight * 0.5,
                    vx: -(Math.random() * 0.6 + 0.3),
                    vy: -(Math.random() * 0.4 + 0.2),
                    radius: Math.random() * 16 + 10,
                    alpha: 0.25,
                    growth: Math.random() * 0.25 + 0.15
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
                p.alpha -= 0.0035;

                if (p.alpha <= 0) {
                    smokeParticles.splice(i, 1);
                    continue;
                }

                const grad = sCtx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius);
                grad.addColorStop(0, `rgba(45, 55, 72, ${p.alpha * 0.5})`);
                grad.addColorStop(1, `rgba(15, 23, 42, 0)`);

                sCtx.fillStyle = grad;
                sCtx.beginPath();
                sCtx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                sCtx.fill();
            }
            requestAnimationFrame(drawSmoke);
        }

        window.addEventListener('resize', resizeSmoke);
        resizeSmoke();
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

        // Check URL Query Parameters for direct scene jumping, e.g. ?step=9 or ?scene=marseille_1
        const urlParams = new URLSearchParams(window.location.search);
        const startStep = urlParams.get('step') || urlParams.get('scene');
        if (startStep !== null) {
            state.prologueActive = false;
            const pStage = document.getElementById('prologueStage');
            if (pStage) pStage.classList.add('hidden');
            const numericStep = parseInt(startStep, 10);
            if (!isNaN(numericStep) && String(numericStep) === startStep.trim()) {
                state.currentStepIndex = numericStep;
            } else {
                const idx = SCENE_SCRIPT.findIndex(s => s.id === startStep.trim());
                state.currentStepIndex = idx !== -1 ? idx : 0;
            }
            renderCurrentStep();
        } else {
            // Start Prologue normally
            renderPrologueSlide();
        }
    </script>
</body>
</html>
'''

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CODE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CODE)

print(f"preview.html and index.html successfully written! Size: {len(HTML_CODE)} characters.")
