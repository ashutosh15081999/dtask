function fetchUser() {
	let searchInput = document.getElementById("searchInput");
	searchInput = searchInput.value;
	location.href = '/user/userlayout/?query=' + searchInput;
}