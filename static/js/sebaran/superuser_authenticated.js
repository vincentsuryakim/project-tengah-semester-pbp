var editModal = document.getElementById('editModal')
editModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-* attributes
    var provinsi = button.getAttribute('data-provinsi')
    var terkonfirmasi = button.getAttribute('data-terkonfirmasi')
    var aktif = button.getAttribute('data-aktif')
    var sembuh = button.getAttribute('data-sembuh')
    var meninggal = button.getAttribute('data-meninggal')
    var pk = button.getAttribute('data-pk')
    
    // Get the modal's content.
    var modalBodyProvinsi = editModal.querySelector('.modal-body .provinsi')
    var modalBodyTerkonfirmasi = editModal.querySelector('.modal-body .terkonfirmasi')
    var modalBodyAktif = editModal.querySelector('.modal-body .aktif')
    var modalBodySembuh = editModal.querySelector('.modal-body .sembuh')
    var modalBodyMeninggal = editModal.querySelector('.modal-body .meninggal')
    var modalSaveButton = editModal.getElementsByClassName("edit-provinsi")

    modalBodyProvinsi.value = provinsi
    modalBodyTerkonfirmasi.value = terkonfirmasi
    modalBodyAktif.value = aktif
    modalBodySembuh.value = sembuh
    modalBodyMeninggal.value = meninggal
    modalSaveButton.pk = pk
})

$(document).ready(function() {
    $(".edit-provinsi").click(function() {
        $.ajax({
            url: "/sebaran/edit",
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            data: {
                "id": editModal.getElementsByClassName("edit-provinsi").pk,
                "provinsi": document.getElementById('modal_provinsi').value,
                "terkonfirmasi": document.getElementById('modal_terkonfirmasi').value,
                "aktif": document.getElementById('modal_aktif').value,
                "sembuh": document.getElementById('modal_sembuh').value,
                "meninggal": document.getElementById('modal_meninggal').value
            },
            success: function(result) {
                location.reload();
            },
            error: function (err) {
                console.error(err)
            }
        })
    })
})