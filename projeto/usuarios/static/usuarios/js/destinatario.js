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
    const params = new URLSearchParams(window.location.search);
    const status = params.get("status");
    const msg = params.get("msg");

    if (status && msg) {
        let popup;

        if (status === "success") {
            popup = document.getElementById("popup-success");
            document.getElementById("popup-success-msg").textContent = msg;
        }
        else if (status === "error") {
            popup = document.getElementById("popup-error");
            document.getElementById("popup-error-msg").textContent = msg;
        }
        else if (status === "info") {
            popup = document.getElementById("popup-info");
            document.getElementById("popup-info-msg").textContent = msg;
        }

        if (popup) {
            popup.style.display = "flex";
            setTimeout(() => { popup.style.display = "none"; }, 5000);
        }
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
