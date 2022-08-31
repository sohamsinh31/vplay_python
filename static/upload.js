let input, hashtagArray, container, t;

input = document.querySelector('#hashtags');
container = document.querySelector('.tag-container');
hashtagArray = [];
let add = document.getElementById("tags");

add.onclick=function(e){
    e.preventDefault();
    if (input.value.length > 0) {
        if (input.value.indexOf('#') == 0) {
            var text = document.createTextNode(input.value);
            var p = document.createElement('p');
            container.appendChild(p);
            p.appendChild(text);
            p.classList.add('tag');
            let tagg = input.value;
            hashtagArray.push(tagg)
            input.value = '';
            console.log(hashtagArray)
            let deleteTags = document.querySelectorAll('.tag');
            for (let i = 0; i < deleteTags.length; i++) {
                deleteTags[i].addEventListener('click', () => {
                    hashtagArray=hashtagArray.filter(itm => itm != deleteTags[i].innerHTML)
                    console.log(hashtagArray)
                    container.removeChild(deleteTags[i]);
                });
            }
        }
        else{
            alert("Please enter # first and then press enter")
            input.value = '';
    }
    }
};

let thumbb,vidd;
$("#thumbb").on('click',function (){
    let thumb1 = document.querySelector('input[name="thumb"]')
    let thumb2 = document.querySelector('input[name="thumb"]').click()
    thumb1.onchange=(e)=>{thumbb=e.target.files[0];$("#th").text(`${e.target.files[0].name}`)}
})
$("#vidd").on('click',function (){
    let vid1 = document.querySelector('input[name="video"]')
    let vid2 = document.querySelector('input[name="video"]').click()
    vid1.onchange=(e)=>{vidd=e.target.files[0];$("#vd").text(`${e.target.files[0].name}`)}
})
$(document).ready(function(){
        $("#sub").click(function () {
        let cate = $("#cate").val();
        let title = $("#title").val();
        let desc = $("#desc").val();
        console.log(hashtagArray)
        var form_data = new FormData();
        // let id =
        form_data.append("thumb",thumbb);
        form_data.append("video",vidd);
        form_data.append("cate",cate);
        form_data.append("title",title);
        form_data.append("desc",desc)
            for (var i = 0; i < hashtagArray.length; i++) {
    form_data.append('arr[]', hashtagArray[i]);
}
        form_data.append("arr",hashtagArray)
       $.ajax({
        url:"http://127.0.0.1:8000/upload/",
        type:"POST",
        data:form_data,
        contentType:false,
        cache:false,
        processData:false,
        success: function(data){
            console.log(data);
        }
       })
    })
});
    //         $.ajax({
    //             url: 'http://' + location.host + '/api/upload/',
    //             type: 'POST',
    //             data: {
    //                 arr:hashtagArray
    //             },
    //             success: function(responce) {
    //                 console.log(responce)
    //                 $("#b2").data(responce)
    //             }
    //         });
    //     });
    // });