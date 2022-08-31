let input, hashtagArray, container, t;

input = document.querySelector('#hashtags');
container = document.querySelector('.tag-container');
hashtagArray = [];
let add = document.getElementById("tags");

add.onclick=function(e){
    e.preventDefault();
    if (input.value.length > 0) {
      var text = document.createTextNode(input.value);
      var p = document.createElement('p');
      container.appendChild(p);
      p.appendChild(text);
      p.classList.add('tag');
      let tagg = "#"+input.value;
      hashtagArray.push(tagg)
      input.value = '';
        console.log(hashtagArray)
      let deleteTags = document.querySelectorAll('.tag');
      for(let i = 0; i < deleteTags.length; i++) {
        deleteTags[i].addEventListener('click', () => {
          container.removeChild(deleteTags[i]);
        });
      }
    }
};
$("#sub").click(function () {
    $('#form1').submit();
});
$(document).ready(function(){
    $("#b1").on("change",function(){
        $.ajax({
            url:location.hostname+'api/upload/',
            type:'get',
            data: {
                btext:$(this).val()
            },
            success:function(responce){
                $("#b2").data(responce)
            }
        });
    });
});