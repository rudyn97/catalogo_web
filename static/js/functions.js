function message_error(obj) {
    var html = '';
    if (typeof(obj) === 'object'){
        html = '<ul style="text-align: left">';
        $.each(obj, function (key, value) {
            html+='<li>'+key+': '+value+'</li>';
            // console.log(key);
            // console.log(value);
        });
        html+='</ul>';
    }else {
        html = '<p>'+obj+'</p>';
    }

    Swal.fire({
            title:'Error:',
            html: html,
            icon:'error'
        });
}

function message_alert(url, title, content, parameters, callback){
    Swal.fire({
  title: title,
  text: content,
  icon: 'info',
  showDenyButton: true,
  showCancelButton: false,
  confirmButtonText: 'Yes',
  denyButtonText: 'No',
  customClass: {
    actions: 'my-actions',
    cancelButton: 'order-1 right-gap',
    confirmButton: 'order-2',
    denyButton: 'order-3',
  }
}).then((result) => {
  if (result.isConfirmed) {
    //Swal.fire('Saved!', '', 'success')
      //PA CDO DIGA SI
      $.ajax({
                url: url, //window.location.pathname
                type: 'POST',
                data: parameters,
                dataType: 'json',
                processData: false,
                contentType: false,
            }).done(function (data) {
                console.log(data);
                if (!data.hasOwnProperty('error')) {
                    //location.href = '{{ list_url }}';
                    callback();
                    return false;
                }
                message_error(data.error);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });

  } else if (result.isDenied) {
    // Swal.fire('Changes are not saved', '', 'info')
  }
})
}
