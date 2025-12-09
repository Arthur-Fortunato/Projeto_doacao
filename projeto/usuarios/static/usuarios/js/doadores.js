document.addEventListener("DOMContentLoaded", function () {

  // NOVA DOAÇÃO 
  const modalDoacao = document.getElementById("modalDoacao");
  const btnNova = document.getElementById("novaDoacaoBtn");
  const fecharModal = document.getElementById("fecharModalDoacao");

  btnNova.addEventListener("click", () => {
    modalDoacao.style.display = "flex";
  });

  fecharModal.addEventListener("click", () => {
    modalDoacao.style.display = "none";
  });

  // EXCLUIR DOAÇÃO 
  const modal = document.getElementById("modalExcluirDoacao");
  const cancelar = document.getElementById("cancelarExcluirDoacao");
  const confirmar = document.getElementById("confirmarExcluirDoacao");

  let idParaExcluir = null;

  document.querySelectorAll(".excluir-doacao").forEach((btn) => {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      idParaExcluir = this.dataset.id;
      modal.style.display = "flex";
    });
  });

  cancelar.addEventListener("click", () => {
    modal.style.display = "none";
    idParaExcluir = null;
  });

  confirmar.addEventListener("click", () => {
    if (idParaExcluir) {
      window.location.href = `/usuarios/doador/excluir/${idParaExcluir}/`;
    }
  });

  window.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.style.display = "none";
      idParaExcluir = null;
    }
  });

  // MODAL: EDITAR DOAÇÃO
  const modalEditar = document.getElementById("modalEditarDoacao");
  const fecharEditar = document.getElementById("fecharModalEditar");
  const formEditar = document.getElementById("formEditar");

  document.querySelectorAll(".editar-doacao").forEach((btn) => {
    btn.addEventListener("click", function (e) {
      e.preventDefault();

      const id = this.dataset.id;
      const tipo = this.dataset.tipo;
      const descricao = this.dataset.descricao;
      const quantidade = this.dataset.quantidade;

      document.getElementById("edit_tipo").value = tipo;
      document.getElementById("edit_descricao").value = descricao;
      document.getElementById("edit_quantidade").value = quantidade;

      formEditar.action = `/usuarios/doador/editar/${id}/`;
      modalEditar.style.display = "flex";
    });
  });

  fecharEditar.addEventListener("click", () => {
    modalEditar.style.display = "none";
  });

  const url = new URLSearchParams(window.location.search);
    const status = url.get("status");
    const msg = url.get("msg");

    if (status && msg) {
        const popup = document.getElementById("popupMessage");
        const popupText = document.getElementById("popupText");

        popupText.textContent = msg;

        popup.classList.remove("popup-success", "popup-error", "popup-info");

        if (status === "success") popup.classList.add("popup-success");
        if (status === "error")   popup.classList.add("popup-error");
        if (status === "info")    popup.classList.add("popup-info");

        popup.style.display = "block";

        setTimeout(() => {
            popup.classList.add("popup-show");
        }, 50);

        setTimeout(() => {
            popup.classList.remove("popup-show");
        }, 2500);

        setTimeout(() => {
            popup.style.display = "none";
        }, 3000);
    }

});

function openTab(tabId, element) {
  document.querySelectorAll(".tab").forEach(tab => {
    tab.classList.remove("active");
  });

  document.querySelectorAll(".nav button").forEach(btn => {
    btn.classList.remove("active");
  });

  const aba = document.getElementById(tabId);
  if (aba) {
    aba.classList.add("active");
  }
  if (element) {
    element.classList.add("active");
  }
}