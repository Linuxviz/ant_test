const ant_space = document.getElementById("ant_space");
const ctx = ant_space.getContext('2d');
const SCALE = 3   // масштаб картинки
const SPACE = 100 // отступ от левого верхнего угла
const rectWith = SCALE;
const rectHeight = SCALE;
const SHIFT_X = (Math.abs(data['start'][0]) - SPACE) * SCALE;
const SHIFT_Y = (Math.abs(data['start'][1]) - SPACE) * SCALE;

// Отрисовка фона
function background_feel() {
    let gradient = ctx.createLinearGradient(0, 0, ant_space.width, ant_space.height);
    gradient.addColorStop(0, "#C7E7F6");
    gradient.addColorStop(1, "#7acef6");
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, ant_space.width, ant_space.height);
}

// Отрисовка отрисовка достижимых клеток
function available_cells_feel() {
    let gradient = ctx.createLinearGradient(0, 0, ant_space.width, ant_space.height);
    gradient.addColorStop(0, "#06e7ec");
    gradient.addColorStop(1, "#087777");
    ctx.fillStyle = gradient;
    data['available_cells'].forEach((array) => {
        ctx.fillRect((array[0] * SCALE) - SHIFT_X, (array[1] * SCALE) - SHIFT_Y, rectWith, rectHeight)
    });
}

// Отрисовка блокирующих клеток
function block_cells_feel() {
    let gradient = ctx.createLinearGradient(0, 0, ant_space.width, ant_space.height);
    gradient.addColorStop(0, "#2f4547");
    gradient.addColorStop(1, "#020101");
    ctx.fillStyle = gradient;
    data['block_cells'].forEach((array) => {
        ctx.fillRect((array[0] * SCALE) - SHIFT_X, (array[1] * SCALE) - SHIFT_Y, rectWith, rectHeight)
    });
}

// Надпись масштаба
function scale_draw() {
    ctx.font = "italic 50pt Arial";
    ctx.fillText('×' + SCALE.toString(), ant_space.width - 50 - SPACE, ant_space.height - SPACE);
}

// Начало координат
function zero_draw() {
    ctx.font = "italic 20pt Arial";
    ctx.fillText(`(${data['start'][0]},${data['start'][1]})`,
        SPACE * SCALE - 55,
        SPACE * SCALE - 15);
}

function arrows() {
    ctx.beginPath();
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 3 * SCALE;
    const start_line = (SPACE * SCALE) * 0.5;
    //правая стрелка
    ctx.moveTo(start_line, start_line);
    ctx.lineTo(start_line + 500, start_line);
    ctx.moveTo(start_line + 480, start_line - 20);
    ctx.lineTo(start_line + 500, start_line);
    ctx.moveTo(start_line + 480, start_line + 20);
    ctx.lineTo(start_line + 500, start_line);
    ctx.font = "italic 20pt Arial";
    ctx.fillText(`X`,
        start_line + 500 - 55,
        start_line - 15);
    //левая стрелка
    ctx.moveTo(start_line, start_line);
    ctx.lineTo(start_line, start_line + 500);
    ctx.moveTo(start_line - 20, start_line + 480);
    ctx.lineTo(start_line, start_line + 500);
    ctx.moveTo(start_line + 20, start_line + 480);
    ctx.lineTo(start_line, start_line + 500);
    ctx.fillText(`Y`,
        start_line - 35,
        start_line + 500 - 45);
    ctx.stroke();
}

background_feel()
available_cells_feel()
block_cells_feel()
scale_draw()
zero_draw()
arrows()

