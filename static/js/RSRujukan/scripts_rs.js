function cari(){
    const input = document.querySelector(".searchbox-input");
    const cards = document.getElementsByClassName("card");
    let filter = input.value.toLowerCase();
    for (let i = 0; i < cards.length; i++) {
        let title = cards[i].querySelector(".card-body");
        if (title.innerText.toLowerCase().indexOf(filter) > -1) {
            cards[i].classList.remove("d-none")
        } else {
            cards[i].classList.add("d-none")
        }
    }
}
