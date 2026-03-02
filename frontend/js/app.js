const API_URL = "/api";

// 1. Login System (index.html)
function handleLogin() {
    const u = document.getElementById('username').value.trim().toLowerCase();
    const p = document.getElementById('password').value;

    // Simple Alpha Auth
    if (u === "alouch" || u === "admin") {
        document.getElementById('loading-overlay').classList.remove('hidden');

        // Simulate secure connection delay for visual effect
        setTimeout(() => {
            sessionStorage.setItem("commander", "Alouch");
            window.location.href = "dashboard";
        }, 2000);
    } else {
        alert("Access Denied. Unauthorized Commander ID.");
    }
}

// Check auth on dashboard load
if (window.location.pathname.includes('dashboard')) {
    const cmdr = sessionStorage.getItem("commander");
    if (!cmdr) {
        window.location.href = "index.html";
    } else {
        if (document.getElementById('user-display')) {
            document.getElementById('user-display').innerText = cmdr;
        }
        // Initial Fetch
        fetchAllData();
        // Update every 30 seconds
        setInterval(fetchAllData, 30000);
    }
}

function logout() {
    sessionStorage.removeItem("commander");
    window.location.href = "index.html";
}

// 2. Tab Navigation
function showTab(id) {
    document.querySelectorAll('.tab-content').forEach(c => {
        c.classList.remove('show');
        setTimeout(() => c.classList.add('hidden'), 300); // Wait for fade out
    });

    document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active-tab'));

    setTimeout(() => {
        const target = document.getElementById('content-' + id);
        target.classList.remove('hidden');
        // Small delay to allow display:block to apply before changing opacity
        setTimeout(() => target.classList.add('show'), 50);
    }, 300);

    document.getElementById('tab-' + id).classList.add('active-tab');
}

// 3. API Fetching Logic
async function fetchAllData() {
    try {
        await Promise.all([
            fetchMarketData(),
            fetchSniperData(),
            fetchPortfolioData()
        ]);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

async function fetchMarketData() {
    try {
        const response = await fetch(`${API_URL}/market`);
        const data = await response.json();

        // Update Crypto (BTC)
        const btc = data.crypto.bitcoin;
        document.getElementById('btc-live').innerText = `$${btc.usd.toLocaleString()}`;
        const btcChangeEl = document.getElementById('btc-change');
        btcChangeEl.innerText = `${btc.usd_24h_change > 0 ? '▲' : '▼'} ${btc.usd_24h_change.toFixed(2)}%`;
        btcChangeEl.className = `text-xs mt-2 font-bold ${btc.usd_24h_change > 0 ? 'text-green-500' : 'text-red-500'}`;

        // Update Gold
        const gold = data.gold;
        document.getElementById('gold-live').innerText = `€ ${gold.gram_24k_eur}`;
        document.getElementById('gold-trend').innerText = gold.trend;

        // Update Forex
        const forex = data.forex.EUR_USD;
        document.getElementById('forex-live').innerText = forex.rate;
        document.getElementById('forex-change').innerText = forex.change;

    } catch (e) {
        console.error("Failed to load market data", e);
    }
}

async function fetchSniperData() {
    try {
        const response = await fetch(`${API_URL}/sniper`);
        const data = await response.json();

        document.getElementById('sniper-status').innerText = data.status;

        const oppContainer = document.getElementById('sniper-opportunities');
        if (data.active_alerts && data.active_alerts.length > 0) {
            oppContainer.innerHTML = ''; // Clear default message
            data.active_alerts.forEach(alert => {
                const color = alert.drop_percentage < -5 ? 'text-red-500' : 'text-yellow-500';
                oppContainer.innerHTML += `
                    <div class="bg-black/80 p-4 rounded-2xl border border-gray-800 flex justify-between items-center hover:border-red-900 transition">
                        <div>
                            <p class="font-bold text-white text-lg">${alert.asset}</p>
                            <p class="${color} font-bold">${alert.status} (${alert.drop_percentage}%)</p>
                        </div>
                        <div class="text-right">
                             <p class="text-xs text-gray-500">Current Entry</p>
                             <p class="text-xl font-black text-green-400">$${alert.price.toLocaleString()}</p>
                             <button onclick="runIntegrityCheck('${alert.asset}')" class="text-xs mt-2 border border-[#D4AF37] text-[#D4AF37] px-3 py-1 rounded">Sixth Sense Analysis</button>
                        </div>
                    </div>
                `;
            });
        }
    } catch (e) {
        console.error("Failed to load sniper data", e);
    }
}

async function fetchPortfolioData() {
    try {
        const response = await fetch(`${API_URL}/portfolio`);
        const data = await response.json();

        // Render Real Estate
        const reContainer = document.getElementById('real-estate-list');
        reContainer.innerHTML = '';
        data.real_estate.forEach(item => {
            reContainer.innerHTML += `
               <div class="bg-black/60 p-6 rounded-[25px] border border-blue-900/30">
                    <p class="text-[10px] text-blue-400 font-bold uppercase mb-1">${item.type}</p>
                    <h3 class="text-xl font-bold text-white mb-2">${item.name}</h3>
                    <p class="text-xs text-gray-400 mb-4">📍 ${item.location}</p>
                    <div class="flex justify-between border-t border-gray-800 pt-4 mt-4">
                        <span class="text-xs text-gray-500">Yield: <strong class="text-green-400">${item.expected_yield}</strong></span>
                        <span class="text-xs text-gray-500">Risk: <strong class="text-white">${item.risk}</strong></span>
                    </div>
                </div>
            `;
        });

        // Render Startups
        const vcContainer = document.getElementById('startups-list');
        vcContainer.innerHTML = '';
        data.startups.forEach(item => {
            vcContainer.innerHTML += `
               <div class="bg-black/60 p-6 rounded-[25px] border border-purple-900/30">
                    <p class="text-[10px] text-purple-400 font-bold uppercase mb-1">${item.sector}</p>
                    <h3 class="text-xl font-bold text-white mb-2">${item.name} <span class="text-xs font-normal text-gray-500">(${item.stage})</span></h3>
                    <p class="text-xs text-gray-400 mb-4 italic">"${item.integrity_check}"</p>
                    <div class="flex justify-between border-t border-gray-800 pt-4 mt-4">
                        <span class="text-xs text-gray-500">Potential: <strong class="text-yellow-400">${item.potential_return}</strong></span>
                        <button onclick="runIntegrityCheck('${item.name}')" class="text-[10px] bg-purple-900/50 text-purple-300 px-2 py-1 rounded">Verify</button>
                    </div>
                </div>
            `;
        });

    } catch (e) {
        console.error("Failed to load portfolio data", e);
    }
}

// 4. Sixth Sense Integrity API Call
async function runIntegrityCheck(assetName) {
    const modal = document.getElementById('integrity-modal');
    const content = document.getElementById('integrity-content');

    modal.classList.remove('hidden');
    content.innerHTML = `<div class="text-center py-8"><div class="spinner mx-auto mb-4"></div><p class="text-gray-400">جاري فحص الأصل وتدقيق السيولة...</p></div>`;

    // Mock payload for the test
    const payload = {
        name: assetName,
        founders_verified: Math.random() > 0.3, // Randomize for demo
        daily_return_promise: Math.random() * 2.0,
        top_holder_share: Math.floor(Math.random() * 60)
    };

    try {
        const response = await fetch(`${API_URL}/integrity_check`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        let detailsHtml = result.details.map(d => `<p class="text-xs text-gray-300 mb-1">• ${d}</p>`).join('');
        if (detailsHtml === '') detailsHtml = '<p class="text-xs text-green-400">لا يوجد إشارات خطر. الأصل يبدو سليماً.</p>';

        const scoreColor = result.score >= 80 ? 'text-green-500' : (result.score >= 50 ? 'text-yellow-500' : 'text-red-500');

        content.innerHTML = `
            <div class="text-center mb-6 border-b border-gray-800 pb-4">
                <p class="text-sm font-bold text-gray-400 uppercase tracking-widest">${assetName}</p>
                <div class="text-6xl font-black ${scoreColor} my-4">${result.score} <span class="text-sm text-gray-500">/ 100</span></div>
                <p class="font-bold text-lg">${result.status}</p>
            </div>
            <div>
                <h4 class="text-[#D4AF37] text-sm mb-2 font-bold">تقرير الحاسة السادسة (Alouch Intel):</h4>
                ${detailsHtml}
            </div>
        `;

    } catch (e) {
        content.innerHTML = `<p class="text-red-500 text-center">فشل الاتصال بالمحرك الخلفي.</p>`;
    }
}

function closeIntegrityModal() {
    document.getElementById('integrity-modal').classList.add('hidden');
}
