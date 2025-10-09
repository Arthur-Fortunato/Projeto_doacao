function openTab(tabId, el) {
    const tabs = document.querySelectorAll(".tab");
    const buttons = document.querySelectorAll(".nav button");

    tabs.forEach(tab => tab.classList.remove("active"));
    buttons.forEach(btn => btn.classList.remove("active"));

    document.getElementById(tabId).classList.add("active");
    el.classList.add("active"); 
}

function setupModal(openBtnId, modalId, closeBtnId) {
    const modal = document.getElementById(modalId);
    const openBtn = document.getElementById(openBtnId);
    const closeBtn = document.getElementById(closeBtnId);

    if (openBtn) {
        openBtn.onclick = () => modal.style.display = "flex";
    }

    if (closeBtn) {
        closeBtn.onclick = () => modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

setupModal("novaDoacaoBtn", "modalDoacao", "fecharModalDoacao");
setupModal("editarPerfilBtn", "modalPerfil", "fecharModalPerfil");
