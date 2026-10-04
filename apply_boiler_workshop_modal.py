# -*- coding: utf-8 -*-
"""
Script to apply the Close-Up Stoking Workshop Modal (with real photo assets)
and in-scene furnace hotspot into build_diegetic_odyssey.py.
"""
import re

with open('build_diegetic_odyssey.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update SCENE_SCRIPT step ship_1
script_needle = """            {
                id: 'ship_1',
                image: 'ship_1_boiler.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 1/5',
                location: 'Hầm Than Tàu Hơi Nước Amiral Latouche-Tréville',
                coords: 'Ấn Độ Dương • Mùa Hè 1911',
                speaker: 'Người Dẫn Truyện',
                role: 'Hầm than tàu hơi nước (Nhiệt độ > 40°C)',
                text: 'Dưới đáy sâu con tàu sắt, nhiệt độ hầm than vượt quá 40 độ C. Bụi than đen bám kín mặt mũi, mồ hôi chảy ròng ròng cay xè mắt. Hãy cầm xẻng sắt xúc đống than dưới sàn đổ vào lò lửa đỏ rực để giữ áp suất cho tàu!',
                action: 'diegetic_boiler'
            },"""

script_replacement = """            {
                id: 'ship_1',
                image: 'ship_1_boiler.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 1/5',
                location: 'Hầm Than Tàu Hơi Nước Amiral Latouche-Tréville',
                coords: 'Ấn Độ Dương • Mùa Hè 1911',
                speaker: 'Văn Ba',
                role: 'Phụ bếp & thợ hầm than (Nhiệt độ > 40°C)',
                text: 'Dưới đáy sâu con tàu, nhiệt độ hầm than vượt quá 40 độ C, bụi than bám đen kịt mặt mũi, mồ hôi chảy ròng ròng cay xè mắt. Áp suất nồi hơi đang sụt giảm nghiêm trọng, ngọn lửa này quyết không được để tắt! Anh bạn, hãy nhấp vào Cửa Lò để giúp tôi xúc than!',
                action: 'open_boiler_hotspot'
            },"""

if script_needle in code:
    code = code.replace(script_needle, script_replacement, 1)
    print("Updated SCENE_SCRIPT step ship_1.")
else:
    print("WARNING: script_needle not found! Checking fallback...")
    # Try finding ship_1 action replacement
    code = re.sub(
        r"id:\s*'ship_1'.*?action:\s*'diegetic_boiler'",
        """id: 'ship_1',
                image: 'ship_1_boiler.jpg',
                act: 'HỒI 3 • HẢI TRÌNH & THẾ GIỚI',
                actIndex: 3,
                sceneNum: 'Cảnh 1/5',
                location: 'Hầm Than Tàu Hơi Nước Amiral Latouche-Tréville',
                coords: 'Ấn Độ Dương • Mùa Hè 1911',
                speaker: 'Văn Ba',
                role: 'Phụ bếp & thợ hầm than (Nhiệt độ > 40°C)',
                text: 'Dưới đáy sâu con tàu, nhiệt độ hầm than vượt quá 40 độ C, bụi than bám đen kịt mặt mũi, mồ hôi chảy ròng ròng cay xè mắt. Áp suất nồi hơi đang sụt giảm nghiêm trọng, ngọn lửa này quyết không được để tắt! Anh bạn, hãy nhấp vào Cửa Lò để giúp tôi xúc than!',
                action: 'open_boiler_hotspot'""",
        code,
        flags=re.DOTALL
    )

# 2. Replace diegeticBoilerRig and add boilerWorkshopModal & furnaceHotspot
boiler_block_pattern = re.compile(
    r"<!-- ======================================================== -->\s*"
    r"<!-- TOP QUEST BANNER.*?<!-- 2\. BẾN CẢNG 1911: SỔ THUYỀN VIÊN",
    re.DOTALL
)

boiler_block_replacement = """        <!-- ======================================================== -->
        <!-- POPUP CẬN CẢNH ĐỐT LÒ HƠI NƯỚC (CLOSE-UP WORKSHOP MODAL CHÂN THỰC 100%) -->
        <!-- ======================================================== -->
        <div id="boilerWorkshopModal" class="hidden absolute inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-3 md:p-6 select-none animate-fade-in">
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
                                Cầm xẻng sắt thật xúc đống than đá đổ vào lò lửa rực hồng để giữ áp suất cho con tàu!
                            </p>
                        </div>
                    </div>

                    <div class="flex items-center gap-3">
                        <!-- Progress counter -->
                        <div class="text-right pl-3 border-l border-amber-500/30 shrink-0">
                            <span class="text-[9px] text-slate-400 font-typewriter uppercase block">Tiến độ xúc than</span>
                            <span id="modalStokeCounter" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 font-typewriter font-bold text-xs border border-amber-500/40">
                                0 / 3 Xẻng
                            </span>
                        </div>
                        <!-- Close button -->
                        <button onclick="closeBoilerModal()" class="p-2 text-slate-400 hover:text-white hover:bg-white/10 rounded-lg transition cursor-pointer" title="Đóng cửa sổ">
                            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                        </button>
                    </div>
                </div>

                <!-- Modal Center Stage: Steam Gauge + Dual Panes (Coal & Furnace) -->
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

                    <!-- Interactive Area: Coal Depot (Left) & Roaring Firebox (Right) -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 h-[300px] md:h-[360px] relative">
                        
                        <!-- Left: Real Anthracite Coal Pile + Real Shovel -->
                        <div id="modalCoalDepot" 
                             onclick="handleModalCoalClick()"
                             class="relative rounded-xl border-2 border-stone-700 bg-stone-950/90 overflow-hidden flex flex-col justify-end p-4 shadow-xl group cursor-pointer hover:border-amber-500/70 transition-all">
                            <!-- Background real coal pile photo -->
                            <img src="assets/coal_pile_real.jpg" alt="Đống Than Thật" 
                                 class="absolute inset-0 w-full h-full object-cover filter contrast-125 brightness-90 group-hover:brightness-100 transition-all">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/30 to-transparent"></div>

                            <!-- Real Shovel overlay sitting on the coal -->
                            <div id="modalShovel" 
                                 onclick="handleModalShovelClick(event)"
                                 class="absolute bottom-4 left-6 w-36 md:w-44 h-56 cursor-grab active:cursor-grabbing transition-transform hover:scale-105 z-20 select-none"
                                 style="touch-action: none;" title="Cầm xẻng xúc than">
                                <img src="assets/shovel_real.png" alt="Xẻng Sắt Thật" 
                                     class="w-full h-full object-contain filter drop-shadow-[0_10px_20px_rgba(0,0,0,1)]">
                                <!-- Glowing Coal payload on shovel blade -->
                                <div id="modalShovelPayload" class="hidden absolute bottom-2 left-6 px-2 py-0.5 rounded-full bg-black/90 border border-orange-500 flex items-center gap-1 shadow-[0_0_15px_rgba(255,100,0,0.9)] animate-pulse">
                                    <span class="text-xs">🪨</span>
                                    <span class="text-[9px] font-typewriter text-orange-400 font-bold uppercase">Đầy Than</span>
                                </div>
                            </div>

                            <div class="relative z-10 pointer-events-none flex items-center justify-between">
                                <span class="px-2.5 py-1 rounded-md bg-black/80 border border-amber-500/50 text-[10px] font-typewriter text-amber-300 uppercase font-bold">
                                    Kho Than Đá (Nhấp để xúc)
                                </span>
                                <span class="text-[10px] text-slate-300 font-typewriter italic">
                                    Than Anthracite
                                </span>
                            </div>
                        </div>

                        <!-- Right: Real Cast-Iron Firebox Door -->
                        <div id="modalFurnaceTarget" 
                             onclick="handleModalFurnaceClick()"
                             class="relative rounded-xl border-2 border-orange-500/60 bg-stone-950 overflow-hidden flex flex-col justify-end p-4 shadow-[0_0_35px_rgba(245,158,11,0.3)] group cursor-pointer hover:border-amber-400 hover:shadow-[0_0_60px_rgba(255,100,0,0.8)] transition-all">
                            <!-- Background real firebox photo -->
                            <img src="assets/firebox_closeup.jpg" alt="Lò Lửa Thật" 
                                 class="absolute inset-0 w-full h-full object-cover filter contrast-125 brightness-105 animate-pulse group-hover:scale-105 transition-transform duration-700">
                            <!-- Heat shimmer overlay -->
                            <div class="absolute inset-0 bg-gradient-to-t from-red-600/30 via-transparent to-transparent pointer-events-none"></div>

                            <div class="relative z-10 pointer-events-none flex items-center justify-between">
                                <span class="px-2.5 py-1 rounded-md bg-black/85 border border-amber-400 text-[10px] font-typewriter text-amber-300 uppercase font-bold shadow-lg">
                                    🔥 Cửa Lò Gang (Thả than vào đây)
                                </span>
                                <span class="text-[10px] text-orange-200 font-typewriter font-bold">
                                    Nhiệt độ > 1,200°C
                                </span>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- Modal Footer Status -->
                <div class="relative z-10 flex items-center justify-between pt-2 border-t border-amber-500/20 text-xs font-typewriter text-slate-400">
                    <div class="flex items-center gap-2">
                        <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
                        <span id="modalFooterHint">Hướng dẫn: Kéo chiếc xẻng hoặc nhấp vào xẻng, sau đó nhấp vào cửa lò than để tiếp nhiên liệu!</span>
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
                    🔥 Nhấp vào đây để xúc than
                </span>
            </div>

            <!-- 2. BẾN CẢNG 1911: SỔ THUYỀN VIÊN"""

if boiler_block_pattern.search(code):
    code = boiler_block_pattern.sub(boiler_block_replacement, code)
    print("Replaced boiler section with boilerWorkshopModal & furnaceHotspot.")
else:
    print("WARNING: boiler_block_pattern not found!")

# 3. Replace shovel and boiler stoking logic with modal logic
modal_logic_pattern = re.compile(
    r"// 5\.1\. Xúc Than Hầm Tàu 40°C.*?// 5\.2\. Sổ Thuyền Viên Bến Cảng 1911",
    re.DOTALL
)

modal_logic_replacement = """// 5.1. Xúc Than Hầm Tàu 40°C: Modal Cận Cảnh Đốt Lò Hơi (Close-Up Workshop)
        let modalShovelHasCoal = false;
        let isDraggingModalShovel = false;
        let modalShovelOffset = { x: 0, y: 0 };

        function openBoilerModal() {
            initAudioContext();
            state.boilerShovelsCount = 0;
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

            const angles = [-45, -10, 25, 70];
            const percents = [35, 55, 80, 100];
            const labels = ['35% (Mức Thấp)', '55% (Đang Tăng)', '80% (Khá Cao)', '100% ĐẠT ĐỈNH (Tối Đa)'];

            const idx = Math.min(state.boilerShovelsCount || 0, 3);
            if (needle) needle.style.transform = `rotate(${angles[idx]}deg)`;
            if (bar) bar.style.width = `${percents[idx]}%`;
            if (valText) valText.textContent = `Áp Suất: ${labels[idx]}`;
            if (counter) counter.textContent = `${idx} / 3 Xẻng`;
        }

        function scoopModalCoal() {
            if (modalShovelHasCoal) return;
            modalShovelHasCoal = true;
            const payload = document.getElementById('modalShovelPayload');
            if (payload) payload.classList.remove('hidden');
            playShovelScrapeSound();
            const hint = document.getElementById('modalFooterHint');
            if (hint) hint.textContent = 'Đã xúc đầy than! Hãy kéo thả hoặc nhấp vào Cửa Lò bên phải để tiếp nhiên liệu!';
        }

        function handleModalShovelClick(e) {
            e.stopPropagation();
            if (!modalShovelHasCoal) {
                scoopModalCoal();
            }
        }

        function handleModalCoalClick() {
            scoopModalCoal();
        }

        function handleModalFurnaceClick() {
            if (modalShovelHasCoal) {
                dropModalCoalIntoFurnace();
            } else {
                scoopModalCoal();
            }
        }

        function dropModalCoalIntoFurnace() {
            modalShovelHasCoal = false;
            const payload = document.getElementById('modalShovelPayload');
            if (payload) payload.classList.add('hidden');
            state.boilerShovelsCount = (state.boilerShovelsCount || 0) + 1;

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

            // Emit sparks from center of furnace
            const fTarget = document.getElementById('modalFurnaceTarget');
            if (fTarget) {
                const rect = fTarget.getBoundingClientRect();
                emitSparks(rect.left + rect.width / 2, rect.top + rect.height / 2, 20);
            }

            // Update UI
            updateModalBoilerUI();

            state.resonance = Math.min(100, state.resonance + 15);
            updateResonanceHUD();

            if (state.boilerShovelsCount >= 3) {
                playShipHorn(0.5);
                const instText = document.getElementById('modalInstructionText');
                const hintText = document.getElementById('modalFooterHint');
                if (instText) instText.innerHTML = '<span class="text-emerald-400 font-bold">HOÀN THÀNH: ÁP SUẤT NỒI HƠI ĐÃ ĐẠT ĐỈNH 100%!</span>';
                if (hintText) hintText.textContent = 'Con tàu rẽ sóng vượt đại dương bao la! Tự động chuyển cảnh...';

                setTimeout(() => {
                    closeBoilerModal();
                    const hotspot = document.getElementById('furnaceHotspot');
                    if (hotspot) hotspot.classList.add('hidden');
                    state.currentStepIndex = 8; // ship_1_dialogue
                    renderCurrentStep();
                }, 1600);
            }
        }

        // Pointer drag support for shovel inside modal
        const modalShovelEl = document.getElementById('modalShovel');
        if (modalShovelEl) {
            modalShovelEl.addEventListener('pointerdown', (e) => {
                initAudioContext();
                isDraggingModalShovel = true;
                modalShovelEl.setPointerCapture(e.pointerId);
                const rect = modalShovelEl.getBoundingClientRect();
                modalShovelOffset.x = e.clientX - rect.left;
                modalShovelOffset.y = e.clientY - rect.top;
                scoopModalCoal();
            });
        }

        window.addEventListener('pointermove', (e) => {
            if (!isDraggingModalShovel || !modalShovelEl) return;
            const newX = e.clientX - modalShovelOffset.x;
            const newY = e.clientY - modalShovelOffset.y;
            modalShovelEl.style.position = 'fixed';
            modalShovelEl.style.left = `${newX}px`;
            modalShovelEl.style.top = `${newY}px`;
            modalShovelEl.style.bottom = 'auto';

            const fTarget = document.getElementById('modalFurnaceTarget');
            if (!fTarget) return;
            const furnaceRect = fTarget.getBoundingClientRect();
            const shovelRect = modalShovelEl.getBoundingClientRect();

            const isOver = (
                shovelRect.right >= furnaceRect.left &&
                shovelRect.left <= furnaceRect.right &&
                shovelRect.bottom >= furnaceRect.top &&
                shovelRect.top <= furnaceRect.bottom
            );

            if (isOver && modalShovelHasCoal) {
                isDraggingModalShovel = false;
                resetModalShovelPos();
                dropModalCoalIntoFurnace();
            }
        });

        window.addEventListener('pointerup', () => {
            if (!isDraggingModalShovel) return;
            isDraggingModalShovel = false;
            resetModalShovelPos();
        });

        function resetModalShovelPos() {
            if (!modalShovelEl) return;
            modalShovelEl.style.position = '';
            modalShovelEl.style.left = '';
            modalShovelEl.style.top = '';
            modalShovelEl.style.bottom = '';
        }

        // 5.2. Sổ Thuyền Viên Bến Cảng 1911"""

if modal_logic_pattern.search(code):
    code = modal_logic_pattern.sub(modal_logic_replacement, code)
    print("Replaced shovel logic with modal logic.")
else:
    print("WARNING: modal_logic_pattern not found!")

# 4. Update handleDiegeticTriggers
trigger_pattern = re.compile(
    r"function handleDiegeticTriggers\(action\)\s*\{.*?if \(action === 'diegetic_boiler'\).*?\} else if \(action === 'diegetic_register'\)",
    re.DOTALL
)

trigger_replacement = """function handleDiegeticTriggers(action) {
            const dialogueBox = document.getElementById('dialogueBox');
            const questBanner = document.getElementById('diegeticQuestBanner');
            const hotspot = document.getElementById('furnaceHotspot');
            const registerRig = document.getElementById('diegeticRegisterRig');
            const unificationRig = document.getElementById('diegeticUnificationRig');
            const milestoneRig = document.getElementById('diegeticMilestoneRig');
            const dawnRig = document.getElementById('diegeticDawnRig');

            // Reset rigs and quest banner by default
            if (hotspot) hotspot.classList.add('hidden');
            if (registerRig) registerRig.classList.add('hidden');
            if (unificationRig) unificationRig.classList.add('hidden');
            if (milestoneRig) milestoneRig.classList.add('hidden');
            if (dawnRig) dawnRig.classList.add('hidden');
            if (questBanner) questBanner.classList.add('hidden');

            // Restore dialogue box by default
            if (dialogueBox) dialogueBox.classList.remove('hidden');

            if (action === 'open_boiler_hotspot' || action === 'diegetic_boiler') {
                // Show pulsing hotspot on furnace door
                if (hotspot) hotspot.classList.remove('hidden');
            } else if (action === 'diegetic_register')"""

if trigger_pattern.search(code):
    code = trigger_pattern.sub(trigger_replacement, code)
    print("Updated handleDiegeticTriggers for open_boiler_hotspot.")
else:
    print("WARNING: trigger_pattern not found!")

with open('build_diegetic_odyssey.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Finished applying modal updates to build_diegetic_odyssey.py!")
