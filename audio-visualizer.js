const canvas = document.getElementById('audioVisualizer');
const canvasCtx = canvas.getContext('2d');

// Definições dos blocos e fileiras
const blockSize = 25; // Tamanho de cada bloco em pixels
const blockSpacing = 1; // Espaçamento entre os blocos
const rows = 8; // Número de blocos em cada fileira vertical
const columns = 28; // Número total de fileiras
const gridColor = 'rgb(20, 20, 20)'; // Cor do grid
const blockColor = 'rgb(0, 0, 0)'; // Cor dos blocos quando não há som
const WIDTH = blockSize * columns + blockSpacing * (columns - 1);
const HEIGHT = blockSize * rows + blockSpacing * (rows - 1);

canvas.width = WIDTH;
canvas.height = HEIGHT;

// Adicionando uma variável de sensibilidade
const sensitivity = 0.9; // Ajuste este valor conforme necessário

// Função para desenhar a grade inicial
function drawGrid() {
  for (let x = 0; x < columns; x++) {
    for (let y = 0; y < rows; y++) {
      canvasCtx.fillStyle = gridColor;
      canvasCtx.fillRect(
        x * (blockSize + blockSpacing),
        y * (blockSize + blockSpacing),
        blockSize,
        blockSize
      );
      canvasCtx.strokeStyle = blockColor;
      canvasCtx.strokeRect(
        x * (blockSize + blockSpacing),
        y * (blockSize + blockSpacing),
        blockSize,
        blockSize
      );
    }
  }
}

// Função para calcular a cor baseada na intensidade do volume
function calculateFireColor(volume, maxVolume) {
  const intensity = volume / maxVolume;
  let color;
  
  if (intensity < 0.3) {
    color = `hsl(38, 100%, ${50 + intensity * 50}%)`;
  } else if (intensity < 0.6) {
    color = `hsl(24, 100%, ${40 + intensity * 40}%)`;
  } else {
    color = `hsl(0, 100%, ${30 + intensity * 30}%)`;
  }

  return color;
}

// Função para colorir os blocos
function colorBlock(x, y, color) {
  canvasCtx.fillStyle = color;
  canvasCtx.fillRect(
    x * (blockSize + blockSpacing),
    y * (blockSize + blockSpacing),
    blockSize,
    blockSize
  );
}

// Inicializar o contexto de áudio
navigator.mediaDevices.getUserMedia({ audio: true, video: false })
.then(function(stream) {
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();
  const analyser = audioContext.createAnalyser();
  const source = audioContext.createMediaStreamSource(stream);
  source.connect(analyser);
  analyser.fftSize = 2048;
  const bufferLength = analyser.frequencyBinCount;
  const dataArray = new Uint8Array(bufferLength);

  function draw() {
    drawGrid(); // Desenha a grade inicial

    analyser.getByteFrequencyData(dataArray);

    let maxVolume = Math.max(...dataArray);

    for (let i = 0; i < bufferLength; i++) {
      const volume = dataArray[i];
      const normalizedVolume = (volume / maxVolume) * sensitivity;
      const blocksToColor = Math.ceil(normalizedVolume * rows);

      for (let y = 0; y < blocksToColor; y++) {
        const color = calculateFireColor(volume, maxVolume);
        colorBlock(i % columns, rows - y - 1, color);
      }
    }

    requestAnimationFrame(draw);
  }

  draw(); // Inicia o loop de desenho
})
.catch(function(err) {
  console.error('Não foi possível obter o stream de áudio:', err);
});
