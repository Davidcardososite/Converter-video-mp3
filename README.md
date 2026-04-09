![Logo](/Converter-video-mp3/conversor-de-video.jpg)
```markdown
# 🎵 YouTube to MP3 Converter Web App

Uma aplicação web moderna e eficiente para converter vídeos do YouTube e outros sites em arquivos MP3 de alta qualidade.

## ✨ Funcionalidades

- 🎵 Conversão de vídeos para MP3 com qualidade ajustável
  - Velocidade de download/conversão (MB/s)
  - Tempo restante estimado
  - Tempo decorrido
- 🎚️ Qualidade de áudio selecionável (64kbps a 320kbps)
- 🧹 Limpeza automática da pasta de uploads (a cada 24 horas)
- 🔒 URLs únicas para cada arquivo convertido
- 📱 Interface responsiva e amigável
- 🚀 Suporte a múltiplos formatos de origem (MP4, WebM, MKV, M4A)

## 🚀 Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Download de Vídeos**: yt-dlp
- **Conversão de Áudio**: FFmpeg
- **Frontend**: HTML/CSS/JavaScript (com Server-Sent Events)
- **Gerenciamento de Progresso**: tqdm

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- **FFmpeg** (obrigatório para conversão de áudio)
```
## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/Converter-video-mp3.git
cd Converter-video-mp3
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install flask yt-dlp tqdm werkzeug
```

### 4. Instale o FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**MacOS:**
```bash
brew install ffmpeg
```

**Windows:**
- Baixe do [site oficial do FFmpeg](https://ffmpeg.org/download.html)
- Adicione ao PATH do sistema

### 5. Configure os cookies (opcional)
- Coloque um arquivo `cookies.txt` na raiz do projeto
- Ajuda a evitar bloqueios e permite acesso a vídeos restritos

## 🎮 Como Usar

1. **Inicie a aplicação**
```bash
python run.py
```

2. **Acesse no navegador**
```
http://localhost:5000
```

3. **Converta um vídeo:**
   - Cole a URL do YouTube (ou site compatível)
   - Selecione a qualidade do MP3 desejada
   - Clique em "Converter"
   - Aguarde o processamento
   - Faça o download do arquivo MP3

## 📁 Estrutura do Projeto

```
youtube-to-mp3/
├── app/
│   ├── __init__.py           # Configuração da aplicação
│   ├── routes.py             # Rotas e lógica principal
│   ├── funcoes.py            # Utilitários (progresso, limpeza)
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── imagens/
│   ├── templates/
│   │   ├── index.html        # Página principal
│   │   ├── termos.html       # Termos de uso
│   │   └── privacidade.html  # Política de privacidade
│   └── uploads/              # Pasta temporária
├── cookies.txt               # Cookies (opcional)
├── run.py                    # Inicialização
├── .gitignore
└── README.md
```

## 🎚️ Qualidades de Áudio Disponíveis

| Qualidade | Bitrate | Uso Recomendado |
|-----------|---------|-----------------|
| Muito Baixa | 64 kbps | Podcasts, audiolivros |
| Baixa | 96 kbps | Economia de espaço |
| **Média (padrão)** | **128 kbps** | **Bom equilíbrio** |
| Alta | 192 kbps | Músicas em geral |
| Muito Alta | 256 kbps | Qualidade superior |
| Máxima | 320 kbps | Audição crítica |

## 🔄 API Endpoints

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/upload_youtube` | POST | Envia URL para conversão |
| `/download/<filename>` | GET | Baixa o MP3 convertido |
| `/progress` | GET | SSE stream do progresso |
| `/termos` | GET | Termos de uso |
| `/privacidade` | GET | Política de privacidade |

## ⚙️ Configurações Avançadas

### Alterar pasta de downloads temporários
```python
# Em routes.py ou __init__.py
UPLOAD_FOLDER = '/caminho/personalizado/uploads'
```

### Modificar intervalo de limpeza
```python
# Em funcoes.py - intervalo em segundos
agendar_limpeza(intervalo=43200)  # 12 horas
```

### Formatos de áudio suportados
O yt-dlp suporta vários formatos além do MP3:
```python
'preferredcodec': 'mp3'     # MP3
'preferredcodec': 'm4a'     # M4A/AAC
'preferredcodec': 'opus'    # Opus
'preferredcodec': 'flac'    # FLAC (sem perdas)
```

## 🐛 Solução de Problemas

### Erro: "FFmpeg não encontrado"
```bash
# Verifique se o FFmpeg está instalado
ffmpeg -version

# Se não estiver, instale conforme instruções acima
```

### Erro de download muito lento
- Use um arquivo `cookies.txt` para melhor performance
- Configure uma VPN/proxy se necessário
- Verifique sua conexão com a internet

### Arquivo MP3 não é gerado
- Certifique-se de que o vídeo não é uma live
- Verifique se o URL é válido
- Confirme se o FFmpeg está funcionando corretamente

### Erro "HTTP Error 403"
- Atualize o arquivo `cookies.txt`
- O vídeo pode ser privado ou com restrição de idade

## 📝 Notas Importantes

- **Direitos Autorais**: Use apenas para conteúdo permitido ou de sua propriedade
- **Armazenamento Temporário**: Arquivos são removidos após 24 horas
- **Limitações**: Não funciona com lives do YouTube
- **Privacidade**: Não armazenamos logs de conversão

## 🛠️ Próximas Funcionalidades (Roadmap)

- [ ] Conversão em lote (múltiplas URLs)
- [ ] Suporte a playlists
- [ ] Extração apenas de trechos (início/fim)
- [ ] Download de capas/thumbnails
- [ ] Metadados ID3 (artista, álbum, capa)
- [ ] Interface com tema escuro
- [ ] Conversão para outros formatos (AAC, OGG, FLAC)
- [ ] Modo offline com cache

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Siga estes passos:

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de código
- Use PEP 8 para Python
- Mantenha os hooks de progresso funcionando
- Teste com diferentes qualidades de áudio

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ⚠️ Aviso Legal

Este software é fornecido "como está", sem garantias. A conversão de conteúdo protegido por direitos autorais pode violar leis em sua jurisdição. O usuário é o único responsável pelo uso desta ferramenta.

**Nota**: Este projeto não hospeda nem distribui conteúdo com direitos autorais - apenas converte vídeos fornecidos pelo usuário.

## 🙏 Agradecimentos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Pela poderosa biblioteca de download
- [FFmpeg](https://ffmpeg.org/) - Pela excelente capacidade de conversão
- [Flask](https://flask.palletsprojects.com/) - Framework web leve e flexível

- ## 📧 Contato

- Email davidcardosodefarias@gmail.com

- [Instagram](https://www.instagram.com/david_cardoso01/)

## 📊 Exemplo de Uso

```python
# Exemplo de requisição via JavaScript
fetch('/upload_youtube', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: 'youtube_url=https://youtube.com/watch?v=...&quality=192'
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        window.location.href = `/download/${data.mp3_filename}`;
    }
});
```

## 🎯 Performance

- **Tamanho médio**: 3-5 MB por minuto (128kbps)
- **Velocidade**: Dependente da conexão e CPU
- **Concorrência**: Suporta múltiplos usuários simultâneos

## 📞 Suporte

- Abra uma issue no GitHub para bugs
- Sugira melhorias via Pull Requests
- Dúvidas: [devdavid1998@gmail.com](mailto:devdavid1998@gmail.com)

---
**Feito com 🎵 e ☕ para a comunidade**
