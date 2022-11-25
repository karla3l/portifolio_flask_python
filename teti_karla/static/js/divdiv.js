for (let i = 1; i <= 512; i++) {
    const box = document.createElement('div')
    box.classList.add('box')
    document.querySelector('.container').appendChild(box)

    for (let i = 1; i <= 512; i++) {
        const box = document.createElement('div')
        box.classList.add('box')
        document.querySelector('.container').appendChild(box)
      }
  }
  
  const btn = document.querySelector('.btn')
  const corAleatoriaBox = document.querySelectorAll('.box')
  
  function hexCorCodigo() {
    var chars = '0123456789abcdef'
    var corTamanho = 6
    var cor = ''
  
    for (var i = 0; i < corTamanho; i++) {
      var corAleatoria = Math.floor(Math.random() * chars.length)
      cor += chars.substring(corAleatoria, corAleatoria + 1)
    }
    return '#' + cor
  }
  
  function addCor() {
    corAleatoriaBox.forEach(e => {
      var novaCor = hexCorCodigo()
      e.style.background = novaCor
      e.innerHTML = novaCor
    })
  }