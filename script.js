let animationsData = {};

// 1. Load Data on Startup
fetch('simulations.json')
    .then(response => response.json())
    .then(data => {
        animationsData = data;
        renderSidebar(); // Initial render
        
        // Load the first simulation by default
        const firstTopic = Object.keys(data)[0];
        const firstSim = Object.keys(data[firstTopic])[0];
        loadSimulation(firstTopic, firstSim);
    });

// 2. Render Sidebar Navigation
function renderSidebar(filterText = "") {
    const navMenu = document.getElementById('navMenu');
    navMenu.innerHTML = ""; // Clear existing

    for (const [topic, sims] of Object.entries(animationsData)) {
        // Check if we should show this topic
        const simKeys = Object.keys(sims);
        const filteredSims = simKeys.filter(name => 
            name.toLowerCase().includes(filterText.toLowerCase())
        );

        if (filteredSims.length > 0) {
            // Create Topic Header if not searching (or if you prefer grouped results)
            if (!filterText) {
                const topicHeader = document.createElement("h4");
                topicHeader.textContent = topic;
                topicHeader.className = "nav-group";
                navMenu.appendChild(topicHeader);
            }

            // Create Links
            filteredSims.forEach(simName => {
                const item = document.createElement("div");
                item.className = "nav-item";
                item.textContent = simName;
                item.onclick = () => {
                    // Remove 'active' class from others
                    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
                    item.classList.add('active');
                    loadSimulation(topic, simName);
                };
                navMenu.appendChild(item);
            });
        }
    }
}

// 3. Search Listener
document.getElementById('searchInput').addEventListener('input', (e) => {
    renderSidebar(e.target.value);
});

// 4. Load Simulation Logic
function loadSimulation(topic, simName) {
    const data = animationsData[topic][simName];

    // Update Text
    document.getElementById('categoryTag').textContent = `Category: ${topic}`;
    document.getElementById('simTitle').textContent = simName;
    document.getElementById('simDescription').innerHTML = data.description; // allow HTML in desc

    // Update Image
    const imgContainer = document.getElementById('imageContainer');
    imgContainer.innerHTML = ""; // Clear previous
    if (data.image && data.image !== "") {
        const img = document.createElement("img");
        img.src = data.image;
        img.className = "diagram";
        imgContainer.appendChild(img);
    }

    // Update Iframe
    document.getElementById('simFrame').src = data.url;

    // Update Questions
    const qContainer = document.getElementById('questionsContainer');
    const qList = document.getElementById('questionsList');
    qList.innerHTML = "";
    
    if (data.questions && data.questions.length > 0 && data.questions[0] !== "") {
        qContainer.style.display = "block";
        data.questions.forEach((q, index) => {
            const p = document.createElement("p");
            p.innerHTML = `<strong>${index + 1}.</strong> ${q}`;
            qList.appendChild(p);
        });
    } else {
        qContainer.style.display = "none";
    }
}
