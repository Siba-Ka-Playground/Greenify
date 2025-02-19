// Side Bar Toogle works
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const content = document.getElementById("content");
  const h_detail = document.getElementById("h_detail");
  const b_detail = document.getElementById("b_detail");
  const r_detail = document.getElementById("r_detail");
  const c_detail = document.getElementById("c_detail");
  sidebar.classList.toggle("open");
  content.classList.toggle("shifted");
  h_detail.classList.toggle("detail");
  b_detail.classList.toggle("detail");
  r_detail.classList.toggle("detail");
  c_detail.classList.toggle("detail");
}
