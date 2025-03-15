
// accordion
var acc = document.getElementsByClassName("accordion");
    for (var i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }




// efeito clean
  const elements = document.querySelectorAll('.search-container2, .logos');

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animated');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0 });

  elements.forEach(element => {
    observer.observe(element);
  });










document.addEventListener('DOMContentLoaded', function() {
    
    const hamburgerIcon = document.querySelector('.botaohamburger');
    
    const botaohamburger1 = document.querySelector('.botaohamburger1');
    const botaohamburger2 = document.querySelector('.botaohamburger2');
    const botaohamburger3 = document.querySelector('.botaohamburger3');
    
    
    const navList = document.querySelector('.nav_list');
    
    
    const imagemseta = document.querySelector('.imagemseta');

    // Adiciona um evento de clique ao ícone do hambúrguer
    hamburgerIcon.addEventListener('click', function(event) {
        event.stopPropagation();
        hamburgerIcon.classList.toggle('open');
        
        
        botaohamburger1.classList.toggle('open');
        botaohamburger2.classList.toggle('open');
        botaohamburger3.classList.toggle('open');
        
        navList.classList.toggle('open');
        
        
    });

    // Adiciona um evento de clique ao documento inteiro
    document.addEventListener('click', function(event) {
        if (!navList.contains(event.target) && navList.classList.contains('open')) {
            
            botaohamburger1.classList.remove('open');
            botaohamburger2.classList.remove('open');
            botaohamburger3.classList.remove('open');
            
            navList.classList.remove('open');
            hamburgerIcon.classList.remove('open');
        }
    });
});

$(document).ready(function(){
    $('#audio_form').on('submit', function(event){
        event.preventDefault();
        var form_data = new FormData($(this)[0]);
        uploadFiles(form_data, '#converted_files_list', '/upload_youtube');
        document.querySelector('.imagem-processando').style.display = 'block';
        // mostrar as animações
        document.querySelector('.convertendo').style.display = 'block';
    });
    
    function uploadFiles(form_data, fileListSelector, url) {
        $(fileListSelector).empty();

        $.ajax({
            type: 'POST',
            url: url,
            data: form_data,
            contentType: false,
            processData: false,
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener("progress", function(evt) {
                }, false);
                return xhr;
            },
            success: function(response) {
                $('.imagem-processando').hide();
                    $('.convertendo').hide();// Esconder a animação em caso de sucesso
                if (response.success) {
                    var mp3_filename = response.mp3_filename;
                    var downloadLink = $('<a class="download-link" href="/download/' + mp3_filename + '">Baixar</a>');
                    $(fileListSelector).append(downloadLink);
                } else {
                    alert('Erro: ' + response.error);
                }
            },
            error: function(xhr, status, error) {
                $('.imagem-processando').hide();
                    $('.convertendo').hide();// Esconder a animação em caso de erro
                alert("Ocorreu um erro durante a solicitação ao servidor: " + error);
            }
        });
    }
});
