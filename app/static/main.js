let click = 0;
let clicks = 0;
function onClick() {
    click += 1;
    document.getElementById("click").innerHTML = click;
}
function onClicks() {
    clicks += 1;
    document.getElementById("clicks").innerHTML = clicks;
}