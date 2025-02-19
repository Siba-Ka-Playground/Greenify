function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const content = document.getElementById("content");
  const h_detail = document.getElementsById("h_detail");
  const b_detail = document.getElementsById("b_detail");
  sidebar.classList.toggle("open");
  content.classList.toggle("shifted");
  h_detail.classList.toggle("detail");
  b_detail.classList.toggle("detail");
}
