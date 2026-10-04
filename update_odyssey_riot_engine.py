# -*- coding: utf-8 -*-
"""
Updater script to upgrade build_diegetic_odyssey.py with Riot Games (LoL) style:
1. Smart HUD: Auto-collapse dialogue box into Top Quest Banner during interactive steps.
2. Hide UI button (H key) inspired by Spirit Blossom.
3. Pixel-perfect Diegetic Boiler Rig matching ship_1_boiler.jpg.
4. Tactile dual drag-and-drop & click-to-stoke mechanics with sound synthesis, sparks, and gauge motion.
"""
import re

with open('build_diegetic_odyssey.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add CSS animations and HUD class
css_needle = '''.diegetic-prop {
            filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.7));
            transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
        }
        .diegetic-prop:hover {
            transform: scale(1.04);
            filter: drop-shadow(0 0 15px rgba(245, 158, 11, 0.8));
        }'''

css_replacement = '''.diegetic-prop {
            filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.7));
            transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
        }
        .diegetic-prop:hover {
            transform: scale(1.04);
            filter: drop-shadow(0 0 15px rgba(245, 158, 11, 0.8));
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
        }'''

if css_needle in code:
    code = code.replace(css_needle, css_replacement, 1)
    print("Replaced CSS animations and classes.")
else:
    print("WARNING: css_needle not found!")

# 2. Add Hide UI button to header
header_needle = '''                <!-- History Log -->
                <button onclick="toggleLogModal(true)" title="Nhật ký hội thoại (Phím L)"
                        class="min-w-[44px] min-h-[44px] p-2.5 rounded-lg border border-brass/40 bg-abyss/80 hover:bg-brass/20 text-brass transition-all flex items-center justify-center cursor-pointer">
                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                </button>
            </div>
        </header>'''

header_replacement = '''                <!-- History Log -->
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
        </header>'''

if header_needle in code:
    code = code.replace(header_needle, header_replacement, 1)
    print("Replaced header with Hide UI button.")
else:
    print("WARNING: header_needle not found!")

# Also mark header with hud-element
code = code.replace('<header class="relative z-20 flex', '<header class="hud-element relative z-20 flex', 1)
# Mark main with hud-element
code = code.replace('<main class="relative z-20 p-4', '<main class="hud-element relative z-20 p-4', 1)

# 3. Replace diegeticBoilerRig and add Top Quest Banner
boiler_rig_start = '        <!-- DIEGETIC IN-SCENE INTERACTIVE STAGE (100% IN-SCENE, NO POPUPS!) -->'
boiler_rig_end = '            <!-- 2. BẾN CẢNG 1911: SỔ THUYỀN VIÊN TRÊN MẶT BÀN GỖ BẾN TÀU -->'

boiler_rig_replacement = '''        <!-- ======================================================== -->
        <!-- TOP QUEST BANNER (CHUẨN RIOT GAMES / LEAGUE OF LEGENDS) -->
        <!-- ======================================================== -->
        <div id="diegeticQuestBanner" class="hidden absolute top-5 left-1/2 -translate-x-1/2 z-40 w-[92%] max-w-2xl px-5 py-3 rounded-2xl bg-black/85 border border-amber-500/70 backdrop-blur-md shadow-[0_15px_40px_rgba(0,0,0,0.95)] flex items-center justify-between pointer-events-auto transition-all duration-300 hud-element select-none">
            <div class="flex items-center gap-3.5">
                <div class="w-9 h-9 rounded-xl bg-amber-500/20 border border-amber-400 flex items-center justify-center text-amber-400 shadow-md shrink-0">
                    <svg id="questIcon" class="w-5 h-5 animate-pulse" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
                <div>
                    <div class="text-xs md:text-sm font-cinematic font-bold text-amber-300 uppercase tracking-widest flex items-center gap-2">
                        <span id="questTitle">NHIỆM VỤ LỊCH SỬ</span>
                        <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                        <span id="questSubtitle" class="text-slate-300 font-normal">HẦM NỒI HƠI TÀU (42°C)</span>
                    </div>
                    <div id="questInstruction" class="text-xs text-amber-100 font-typewriter mt-0.5">
                        Kéo xẻng sắt xúc đống than dưới sàn đổ vào lò lửa để tăng áp suất hơi nước
                    </div>
                </div>
            </div>
            <div class="flex items-center gap-2 pl-4 border-l border-amber-500/30 shrink-0">
                <div class="text-right">
                    <span class="text-[9px] text-slate-400 font-typewriter uppercase block">Tiến độ</span>
                    <span id="questCounter" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 font-typewriter font-bold text-xs border border-amber-500/40">
                        0 / 3 Xẻng
                    </span>
                </div>
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- DIEGETIC IN-SCENE INTERACTIVE STAGE (100% IN-SCENE, NO POPUPS!) -->
        <!-- ======================================================== -->
        <div id="diegeticLayer" class="absolute inset-0 z-15 pointer-events-none">
            
            <!-- ---------------------------------------------------- -->
            <!-- 1. HẦM THAN 40°C: ĐỐNG THAN, XẺNG SẮT & CỬA LÒ TRỰC TIẾP TRÊN PHÔNG NỀN -->
            <!-- ---------------------------------------------------- -->
            <div id="diegeticBoilerRig" class="hidden absolute inset-0 pointer-events-auto select-none">
                <!-- Cửa lò than: Drop Zone hòa nhập hoàn hảo vào bức tranh nền ship_1_boiler.jpg -->
                <div id="diegeticFurnace" 
                     onclick="handleFurnaceClick()"
                     class="absolute top-[44%] right-[19%] md:right-[21%] w-48 md:w-56 h-40 md:h-48 rounded-xl border-2 border-amber-500/50 hover:border-amber-400 hover:shadow-[0_0_50px_rgba(245,158,11,0.9)] flex flex-col items-center justify-end p-2 cursor-pointer transition-all duration-300 group">
                    <!-- Nhiệt lượng tỏa sáng từ lòng lò -->
                    <div class="absolute inset-1 bg-gradient-to-t from-red-600/30 via-orange-500/20 to-amber-300/10 rounded-lg filter blur-xs animate-pulse pointer-events-none"></div>
                    <div class="relative z-10 text-center pointer-events-none pb-1">
                        <span class="text-[10px] md:text-xs font-typewriter uppercase text-amber-200 font-bold tracking-widest drop-shadow-[0_2px_4px_rgba(0,0,0,1)] bg-black/70 px-2.5 py-1 rounded border border-amber-500/40 group-hover:border-amber-400 group-hover:text-amber-100 transition-all">
                            🔥 Cửa Lò [Thả than vào đây]
                        </span>
                    </div>
                </div>

                <!-- Đồng hồ áp suất hơi nước bằng đồng thau trên vách lò -->
                <div id="diegeticGauge" class="absolute top-[17%] right-[19%] md:right-[21%] p-2 rounded-full bg-gradient-to-br from-amber-950 via-stone-900 to-black border-2 border-amber-500/80 shadow-[0_10px_30px_rgba(0,0,0,0.95)] flex flex-col items-center select-none z-20">
                    <div class="w-18 h-18 md:w-20 md:h-20 rounded-full bg-[#f4ecd8] border-2 border-amber-900 flex items-center justify-center relative shadow-inner">
                        <!-- Vạch đo áp suất -->
                        <svg class="absolute inset-0 w-full h-full p-1" viewBox="0 0 100 100">
                            <circle cx="50" cy="50" r="42" fill="none" stroke="#78350f" stroke-width="2" stroke-dasharray="2 6"/>
                            <!-- Vạch đỏ áp suất tối đa -->
                            <path d="M 50 8 A 42 42 0 0 1 85 30" fill="none" stroke="#dc2626" stroke-width="4"/>
                            <text x="50" y="32" font-size="8" text-anchor="middle" font-family="monospace" fill="#78350f" font-weight="bold">STEAM</text>
                            <text x="50" y="75" font-size="7" text-anchor="middle" font-family="monospace" fill="#991b1b" font-weight="bold">kg/cm²</text>
                        </svg>
                        <!-- Kim đo áp suất -->
                        <div id="steamPressureNeedle" class="w-1 h-8 bg-red-700 origin-bottom transform -rotate-45 transition-transform duration-700 ease-out shadow"></div>
                        <div class="absolute w-3 h-3 rounded-full bg-stone-900 border border-amber-600"></div>
                    </div>
                    <span id="gaugeLabel" class="text-[8px] md:text-[9px] font-typewriter text-amber-300 uppercase font-bold mt-1 tracking-wider">
                        Áp Suất: <span id="gaugeValueText">35%</span>
                    </span>
                </div>

                <!-- Đống than trên sàn sắt: Nằm ngay trên đống than của tranh vẽ -->
                <div id="diegeticCoalPile" 
                     onclick="handleCoalPileClick()"
                     class="absolute bottom-[10%] left-[26%] md:left-[30%] w-64 md:w-76 flex flex-col items-center cursor-pointer group z-20">
                    <!-- Hiệu ứng viền sáng nhẹ khi hover -->
                    <div class="relative w-full h-24 flex items-end justify-center">
                        <svg class="w-full h-full filter drop-shadow-[0_10px_25px_rgba(0,0,0,1)] transition-transform group-hover:scale-105" viewBox="0 0 240 100" fill="none">
                            <ellipse cx="120" cy="75" rx="110" ry="22" fill="#0c0a09" opacity="0.95"/>
                            <polygon points="30,80 60,40 100,75" fill="#1c1917" stroke="#292524" stroke-width="1.5"/>
                            <polygon points="80,75 120,25 160,80" fill="#171412" stroke="#44403c" stroke-width="1.5"/>
                            <polygon points="140,78 175,45 210,80" fill="#1c1917" stroke="#292524" stroke-width="1.5"/>
                            <circle cx="115" cy="48" r="4" fill="#ea580c" opacity="0.8" class="animate-ping"/>
                            <circle cx="145" cy="62" r="3" fill="#f97316" opacity="0.9"/>
                            <circle cx="75" cy="58" r="3.5" fill="#f97316" opacity="0.7"/>
                        </svg>
                        <div class="absolute -bottom-2 text-center pointer-events-none">
                            <span class="text-[9px] font-typewriter uppercase text-amber-300 bg-black/80 px-2.5 py-0.5 rounded border border-amber-500/50 group-hover:border-amber-400 group-hover:bg-amber-950/90 transition-all shadow-lg">
                                Đống Than Tàu • Nhấp / Kéo Xẻng Xúc
                            </span>
                        </div>
                    </div>
                </div>

                <!-- Chiếc xẻng sắt cán dài nằm cạnh đống than -->
                <div id="diegeticShovel" 
                     onclick="handleShovelClick(event)"
                     class="absolute bottom-[18%] left-[32%] md:left-[35%] w-52 h-16 flex items-center cursor-grab active:cursor-grabbing transform -rotate-15 hover:rotate-0 transition-transform duration-200 select-none z-30 diegetic-prop"
                     style="touch-action: none;" title="Kéo xẻng hoặc nhấp để xúc than">
                    <!-- Cán xẻng gỗ mun -->
                    <div class="w-38 h-3.5 bg-gradient-to-r from-amber-950 via-amber-800 to-stone-700 rounded-l border border-black shadow-lg"></div>
                    <!-- Lưỡi xẻng sắt rèn chịu lực -->
                    <div id="shovelBlade" class="w-16 h-14 -ml-1 rounded-r-xl bg-gradient-to-r from-stone-700 via-stone-800 to-stone-900 border-2 border-amber-500/70 flex items-center justify-center relative shadow-2xl">
                        <!-- Khối than xúc trên lưỡi xẻng -->
                        <div id="shovelCoalPayload" class="hidden flex items-center justify-center relative">
                            <span class="text-xs">🪨</span>
                            <div class="w-4 h-4 rounded-full bg-orange-600 animate-ping absolute opacity-75"></div>
                        </div>
                    </div>
                </div>
            </div>

'''

pattern = re.compile(re.escape(boiler_rig_start) + '.*?' + re.escape(boiler_rig_end), re.DOTALL)
if pattern.search(code):
    code = pattern.sub(boiler_rig_replacement + '            <!-- 2. BẾN CẢNG 1911: SỔ THUYỀN VIÊN TRÊN MẶT BÀN GỖ BẾN TÀU -->', code)
    print("Replaced diegeticBoilerRig and added Top Quest Banner.")
else:
    print("WARNING: boiler_rig pattern not matched!")

# 4. Add Audio synthesis for shovel, steam release, and gauge tick
sound_needle = '''        function playFurnaceSound() {
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
            nGain.gain.exponentialRampToValueAtTime(0.26, t + 0.25);
            nGain.gain.exponentialRampToValueAtTime(0.001, t + 1.5);

            src.connect(filter);
            filter.connect(nGain);
            nGain.connect(audioCtx.destination);
            src.start(t);
        }'''

sound_replacement = '''        function playShovelScrapeSound() {
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
        }'''

if sound_needle in code:
    code = code.replace(sound_needle, sound_replacement, 1)
    print("Replaced audio synthesis functions.")
else:
    print("WARNING: sound_needle not found!")

# 5. Replace Shovel dragging & stoking logic
shovel_start = '        // 5.1. Xúc Than Hầm Tàu 40°C (Diegetic Shovel & Coal Pile)'
shovel_end = '        // 5.2. Sổ Thuyền Viên Bến Cảng 1911 (Diegetic Register)'

shovel_replacement = '''        // 5.1. Xúc Than Hầm Tàu 40°C (Diegetic Shovel & Coal Pile Chuẩn Riot Games)
        const insceneShovel = document.getElementById('diegeticShovel');
        const coalPayload = document.getElementById('shovelCoalPayload');
        let isDraggingShovel = false;
        let shovelOffset = { x: 0, y: 0 };
        let shovelHasCoal = false;

        function resetShovelPosition() {
            if (!insceneShovel) return;
            insceneShovel.style.left = '';
            insceneShovel.style.top = '';
            insceneShovel.style.bottom = '';
            insceneShovel.style.transform = '';
            shovelHasCoal = false;
            if (coalPayload) coalPayload.classList.add('hidden');
        }

        function scoopCoal() {
            if (shovelHasCoal) return;
            shovelHasCoal = true;
            if (coalPayload) coalPayload.classList.remove('hidden');
            playShovelScrapeSound();
            if (insceneShovel) {
                insceneShovel.classList.add('scale-110');
                setTimeout(() => insceneShovel.classList.remove('scale-110'), 300);
            }
            const bannerInst = document.getElementById('questInstruction');
            if (bannerInst) bannerInst.textContent = 'Đã xúc đầy than! Hãy kéo thả vào Cửa Lò bên phải để tiếp lửa!';
        }

        function handleShovelClick(e) {
            e.stopPropagation();
            if (!shovelHasCoal) {
                scoopCoal();
            }
        }

        function handleCoalPileClick() {
            scoopCoal();
        }

        function handleFurnaceClick() {
            if (shovelHasCoal) {
                const furnaceRect = document.getElementById('diegeticFurnace').getBoundingClientRect();
                dropCoalIntoFurnace(furnaceRect.left + furnaceRect.width / 2, furnaceRect.top + furnaceRect.height / 2);
            } else {
                scoopCoal();
            }
        }

        if (insceneShovel) {
            insceneShovel.addEventListener('pointerdown', (e) => {
                initAudioContext();
                isDraggingShovel = true;
                insceneShovel.setPointerCapture(e.pointerId);
                const rect = insceneShovel.getBoundingClientRect();
                shovelOffset.x = e.clientX - rect.left;
                shovelOffset.y = e.clientY - rect.top;
                
                // Automatically scoop coal when picked up
                scoopCoal();
            });
        }

        window.addEventListener('pointermove', (e) => {
            if (!isDraggingShovel || !insceneShovel) return;
            const newX = e.clientX - shovelOffset.x;
            const newY = e.clientY - shovelOffset.y;
            insceneShovel.style.left = `${newX}px`;
            insceneShovel.style.top = `${newY}px`;
            insceneShovel.style.bottom = 'auto';

            // Check collision with furnace door
            const furnaceRect = document.getElementById('diegeticFurnace').getBoundingClientRect();
            const bladeRect = document.getElementById('shovelBlade').getBoundingClientRect();

            const isOverFurnace = (
                bladeRect.right >= furnaceRect.left &&
                bladeRect.left <= furnaceRect.right &&
                bladeRect.bottom >= furnaceRect.top &&
                bladeRect.top <= furnaceRect.bottom
            );

            if (isOverFurnace && shovelHasCoal) {
                dropCoalIntoFurnace(furnaceRect.left + furnaceRect.width / 2, furnaceRect.top + furnaceRect.height / 2);
            }
        });

        window.addEventListener('pointerup', () => {
            if (!isDraggingShovel) return;
            isDraggingShovel = false;
        });

        function dropCoalIntoFurnace(sparkX, sparkY) {
            shovelHasCoal = false;
            if (coalPayload) coalPayload.classList.add('hidden');
            state.boilerShovelsCount = (state.boilerShovelsCount || 0) + 1;

            playFurnaceSound();
            playSteamReleaseSound();
            playGaugeTickSound();
            emitSparks(sparkX, sparkY, 15);

            // Screen rumble effect
            const stage = document.getElementById('theaterStage');
            if (stage) {
                stage.classList.remove('animate-rumble');
                void stage.offsetWidth;
                stage.classList.add('animate-rumble');
            }

            // Needle increments: 0 -> -45deg, 1 -> -10deg (55%), 2 -> 25deg (80%), 3 -> 70deg (100% MAX)
            const needle = document.getElementById('steamPressureNeedle');
            const gaugeText = document.getElementById('gaugeValueText');
            const angles = [-45, -10, 25, 70];
            const percents = ['35%', '55%', '80%', '100% ĐẠT ĐỈNH'];
            const curIdx = Math.min(state.boilerShovelsCount, 3);
            if (needle) needle.style.transform = `rotate(${angles[curIdx]}deg)`;
            if (gaugeText) gaugeText.textContent = percents[curIdx];

            // Visual feedback on furnace
            const furnace = document.getElementById('diegeticFurnace');
            if (furnace) {
                furnace.classList.add('ring-4', 'ring-amber-400', 'scale-105', 'shadow-[0_0_60px_rgba(255,100,0,1)]');
                setTimeout(() => furnace.classList.remove('ring-4', 'ring-amber-400', 'scale-105', 'shadow-[0_0_60px_rgba(255,100,0,1)]'), 600);
            }

            // Update quest counter
            const counterEl = document.getElementById('questCounter');
            if (counterEl) counterEl.textContent = `${state.boilerShovelsCount} / 3 Xẻng`;

            resetShovelPosition();

            state.resonance = Math.min(100, state.resonance + 15);
            updateResonanceHUD();

            if (state.boilerShovelsCount >= 3) {
                const questTitle = document.getElementById('questTitle');
                const questInst = document.getElementById('questInstruction');
                if (questTitle) questTitle.innerHTML = '<span class="text-emerald-400 font-bold">HOÀN THÀNH NHIỆM VỤ</span>';
                if (questInst) questInst.textContent = 'Áp suất nồi hơi đã đạt 100%! Con tàu rẽ sóng vượt đại dương bao la!';
                playShipHorn(0.5);

                setTimeout(() => {
                    document.getElementById('diegeticBoilerRig').classList.add('hidden');
                    document.getElementById('diegeticQuestBanner').classList.add('hidden');
                    state.currentStepIndex = 8; // ship_1_dialogue
                    renderCurrentStep();
                }, 1600);
            }
        }

'''

pattern_shovel = re.compile(re.escape(shovel_start) + '.*?' + re.escape(shovel_end), re.DOTALL)
if pattern_shovel.search(code):
    code = pattern_shovel.sub(shovel_replacement + '        // 5.2. Sổ Thuyền Viên Bến Cảng 1911 (Diegetic Register)', code)
    print("Replaced shovel and boiler stoking logic.")
else:
    print("WARNING: shovel pattern not matched!")

# 6. Replace handleDiegeticTriggers
trigger_needle = '''        function handleDiegeticTriggers(action) {
            // Hide all diegetic rigs by default
            document.getElementById('diegeticBoilerRig').classList.add('hidden');
            document.getElementById('diegeticRegisterRig').classList.add('hidden');
            document.getElementById('diegeticUnificationRig').classList.add('hidden');
            document.getElementById('diegeticMilestoneRig').classList.add('hidden');
            document.getElementById('diegeticDawnRig').classList.add('hidden');

            if (action === 'diegetic_boiler') {
                document.getElementById('diegeticBoilerRig').classList.remove('hidden');
            } else if (action === 'diegetic_register') {
                document.getElementById('diegeticRegisterRig').classList.remove('hidden');
            } else if (action === 'play_horn') {
                playShipHorn(0.35);
            } else if (action === 'diegetic_unification') {
                document.getElementById('diegeticUnificationRig').classList.remove('hidden');
            } else if (action === 'diegetic_milestone') {
                document.getElementById('diegeticMilestoneRig').classList.remove('hidden');
            } else if (action === 'diegetic_dawn') {
                playDawnBloomChord();
                document.getElementById('diegeticDawnRig').classList.remove('hidden');
            }
        }'''

trigger_replacement = '''        function handleDiegeticTriggers(action) {
            const dialogueBox = document.getElementById('dialogueBox');
            const questBanner = document.getElementById('diegeticQuestBanner');
            const boilerRig = document.getElementById('diegeticBoilerRig');
            const registerRig = document.getElementById('diegeticRegisterRig');
            const unificationRig = document.getElementById('diegeticUnificationRig');
            const milestoneRig = document.getElementById('diegeticMilestoneRig');
            const dawnRig = document.getElementById('diegeticDawnRig');

            // Hide all diegetic rigs and quest banner by default
            boilerRig.classList.add('hidden');
            registerRig.classList.add('hidden');
            unificationRig.classList.add('hidden');
            milestoneRig.classList.add('hidden');
            dawnRig.classList.add('hidden');
            questBanner.classList.add('hidden');

            // Restore dialogue box by default
            dialogueBox.classList.remove('hidden');

            if (action === 'diegetic_boiler') {
                // HIDE dialogue box to prevent blocking
                dialogueBox.classList.add('hidden');
                // SHOW Top Quest Banner
                questBanner.classList.remove('hidden');
                document.getElementById('questTitle').textContent = 'NHIỆM VỤ LỊCH SỬ';
                document.getElementById('questSubtitle').textContent = 'HẦM NỒI HƠI LATOUCHE-TRÉVILLE (42°C)';
                document.getElementById('questInstruction').textContent = 'Cầm xẻng sắt xúc than dưới sàn đổ vào lò lửa để tăng áp suất tàu (hoặc nhấp xẻng rồi nhấp lò)';
                document.getElementById('questCounter').textContent = `${state.boilerShovelsCount || 0} / 3 Xẻng`;
                boilerRig.classList.remove('hidden');
                resetShovelPosition();
            } else if (action === 'diegetic_register') {
                dialogueBox.classList.add('hidden');
                questBanner.classList.remove('hidden');
                document.getElementById('questTitle').textContent = 'THỦ TỤC XUẤT BẾN';
                document.getElementById('questSubtitle').textContent = 'BẾN NHÀ RỒNG • 05/06/1911';
                document.getElementById('questInstruction').textContent = 'Ký tên vào Sổ Thuyền Viên để nhận danh phận thủy thủ "Văn Ba" bước lên tàu';
                document.getElementById('questCounter').textContent = 'Chờ ký tên';
                registerRig.classList.remove('hidden');
            } else if (action === 'diegetic_unification') {
                dialogueBox.classList.add('hidden');
                questBanner.classList.remove('hidden');
                document.getElementById('questTitle').textContent = 'HỢP NHẤT LỊCH SỬ';
                document.getElementById('questSubtitle').textContent = 'HƯƠNG CẢNG • 03/02/1930';
                document.getElementById('questInstruction').textContent = 'Nhấp nút hợp nhất để hòa quyện 3 tổ chức thành một Đảng duy nhất';
                document.getElementById('questCounter').textContent = 'Chờ hợp nhất';
                unificationRig.classList.remove('hidden');
            } else if (action === 'diegetic_milestone') {
                dialogueBox.classList.add('hidden');
                questBanner.classList.remove('hidden');
                document.getElementById('questTitle').textContent = 'MÙA XUÂN TRỞ VỀ';
                document.getElementById('questSubtitle').textContent = 'CỘT MỐC 108 PÁC BÓ • 1941';
                document.getElementById('questInstruction').textContent = 'Chạm tay vào Cột Mốc 108 để cảm nhận hơi ấm thiêng liêng của đất mẹ';
                document.getElementById('questCounter').textContent = 'Chạm cột mốc';
                milestoneRig.classList.remove('hidden');
            } else if (action === 'diegetic_dawn') {
                playDawnBloomChord();
                dawnRig.classList.remove('hidden');
            } else if (action === 'play_horn') {
                playShipHorn(0.35);
            }
        }'''

if trigger_needle in code:
    code = code.replace(trigger_needle, trigger_replacement, 1)
    print("Replaced handleDiegeticTriggers with Smart HUD logic.")
else:
    print("WARNING: trigger_needle not found!")

# 7. Add Hide UI logic and keyboard shortcut H
state_needle = '        const state = {'
state_replacement = '''        function toggleHideUI() {
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

        const state = {
            isUIHidden: false,'''

if state_needle in code:
    code = code.replace(state_needle, state_replacement, 1)
    print("Added toggleHideUI and state.isUIHidden.")
else:
    print("WARNING: state_needle not found!")

# Keyboard shortcut H
key_needle = '''            } else if (e.key.toLowerCase() === 'r') {
                restartExperience();'''

key_replacement = '''            } else if (e.key.toLowerCase() === 'h') {
                toggleHideUI();
            } else if (e.key.toLowerCase() === 'r') {
                restartExperience();'''

if key_needle in code:
    code = code.replace(key_needle, key_replacement, 1)
    print("Added H shortcut for toggleHideUI.")
else:
    print("WARNING: key_needle not found!")

with open('build_diegetic_odyssey.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated build_diegetic_odyssey.py!")
