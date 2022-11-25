$(document).ready(function(){
  var ponteiro =  $(".ponteiro:first");
  $("#btnClone").on('click', function(){
  $('body').append($(ponteiro).clone(true));
  });

  function click() {
    ponteiro = original.clone(true);
    i = i + ponteiro*512;
    console.log(ponteiro);
}
   for(i = 0; i < 10; i++) {
    click();
}
const size = 512
const divs = new Array(size)

for (let i = 0; i < size; i++) {
  divs[i] = {
    id: i,
    divs: `Divs ${i}`
  }
}

});

