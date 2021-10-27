var sebaranUserModal = document.getElementById('editSebaranUserModal')
sebaranUserModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-* attributes
    var provinsi = button.getAttribute('data-provinsi')
    
    // Get the modal's content.
    var modalBodyProvinsi = sebaranUserModal.querySelector('.modal-body .provinsi')

    modalBodyProvinsi.value = provinsi
})

$(document).ready(function() {
    $(".add-sebaranuser").click(function() {
        if (!!document.getElementById('modal_provinsi_sebaran_add').value) {
            $.ajax({
                url: "/sebaran/edit-user",
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                data: {
                    "provinsi": document.getElementById('modal_provinsi_sebaran_add').value
                },
                success: function(result) {
                    location.reload();
                },
                error: function(err) {
                    console.error(err)
                }
            })
        } else {
            console.error("Anda belum memilih provinsi")
        }
    })

    $(".edit-sebaranuser").click(function() {
        if (!!document.getElementById('modal_provinsi_sebaran_edit').value) {
            $.ajax({
                url: "/sebaran/edit-existing-user",
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                data: {
                    "provinsi": document.getElementById('modal_provinsi_sebaran_edit').value
                },
                success: function(result) {
                    location.reload();
                },
                error: function(err) {
                    console.error(err)
                }
            })
        } else {
            console.error("Anda belum memilih provinsi")
        }
    })

    $(".hapus-sebaranuser").click(function() {
        $.ajax({
            url: "/sebaran/delete-user",
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            success: function(result) {
                location.reload();
            },
            error: function(err) {
                console.error(err)
            }
        })
    })
})