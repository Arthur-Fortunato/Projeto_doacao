document.addEventListener("DOMContentLoaded", function() {
    // Modal
    const abrir = document.getElementById("abrirModal");
    const modal = document.getElementById("modalSolicitacao");
    const fechar = document.getElementById("fecharModal");

    abrir.addEventListener("click", () => modal.style.display = "flex");
    fechar.addEventListener("click", () => modal.style.display = "none");

    window.addEventListener("click", (e) => {
        if (e.target === modal) modal.style.display = "none";
    });

    // Popup 
    const url = new URLSearchParams(window.location.search);
    const status = url.get("status");
    const msg = url.get("msg");

    if (status && msg) {
        const popup = document.getElementById("popupMessage");
        const text = document.getElementById("popupText");

        text.textContent = msg;

        popup.classList.add("popup-show");

        if (status === "success") popup.classList.add("popup-success");
        if (status === "error")   popup.classList.add("popup-error");
        if (status === "info")    popup.classList.add("popup-info");

        popup.style.display = "block";

        setTimeout(() => popup.classList.remove("popup-show"), 2500);
        setTimeout(() => popup.style.display = "none", 3000);
    }

    const modalExcluir = document.getElementById("modalExcluir");
    const cancelarExclusao = document.getElementById("cancelarExclusao");
    const confirmarExclusao = document.getElementById("confirmarExclusao");
    let idParaExcluir = null;

    // quando clicar no ícone da lixeira
    document.querySelectorAll(".excluir").forEach(botao => {
        botao.addEventListener("click", function(e) {
            e.preventDefault();
            idParaExcluir = this.getAttribute("data-id");  
            modalExcluir.style.display = "flex";
        });
    });

    // cancelar exclusão
    cancelarExclusao.addEventListener("click", () => {
        modalExcluir.style.display = "none";
        idParaExcluir = null;
    });

    // confirmar exclusão
    confirmarExclusao.addEventListener("click", () => {
        if (idParaExcluir) {
            window.location.href = `/usuarios/destinatario/excluir/${idParaExcluir}/`;
        }
    });

    // fechar clicando fora
    window.addEventListener("click", (e) => {
        if (e.target === modalExcluir) {
            modalExcluir.style.display = "none";
            idParaExcluir = null;
        }
    });
});
