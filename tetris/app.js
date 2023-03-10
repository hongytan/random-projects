document.addEventListener('DOMContentLoaded', () => {

    const grid = document.querySelector('.grid')
    let squares = Array.from(document.querySelectorAll('.grid div'))
    console.log(squares)
    const width = 10    
    const scoreDisplay = document.querySelector('#score')
    const startBtn = document.querySelector('#start-button')
    let nextRandom = 0
    let score = 0
    let timerId
    const colors = ['orange', 'red', 'purple', 'green', 'blue']

    // Tetrominoes
    const L = [
        [1, width+1, 2*width+1, 2],
        [width, width+1, width+2, 2*width+2],
        [1, width+1, 2*width+1, 2*width],
        [width, 2*width, 2*width+1, 2*width+2]
    ]

    const Z = [
        [width+1, width+2, 2*width, 2*width+1],
        [0, width, width+1, 2*width+1],
        [width+1, width+2, 2*width, 2*width+1],
        [0, width, width+1, 2*width+1]
    ]

    const T = [
        [1, width, width+1, width+2],
        [1, width+1, width+2, 2*width+1],
        [width, width+1, width+2, 2*width+1],
        [1, width, width+1, 2*width+1]
    ]

    const O = [
        [0,1, width, width+1],
        [0,1, width, width+1],
        [0,1, width, width+1],
        [0,1, width, width+1]
    ]

    const I = [
        [1, width+1, 2*width+1, 3*width+1],
        [width, width+1, width+2, width+3],
        [1, width+1, 2*width+1, 3*width+1],
        [width, width+1, width+2, width+3]
    ]

    const Tetrominoes = [L,Z,T,O,I]

    let currentPosition = 3
    let currentRotation = 0

    let random = Math.floor(Math.random()*Tetrominoes.length)
    let currentTetromino = Tetrominoes[random][currentRotation]

    function draw() {
        currentTetromino.forEach(index => {
            squares[currentPosition + index].classList.add('tetromino')
            squares[currentPosition + index].style.backgroundColor = colors[random]
        })
    }

    function undraw() {
        currentTetromino.forEach(index => {
            squares[currentPosition + index].classList.remove('tetromino')
            squares[currentPosition + index].style.backgroundColor = ''
        })
    }

    function control(e) {
        if (e.keyCode === 37) {
            moveLeft()
        }
        if (e.keyCode === 38) {
            rotate()
        }
        if (e.keyCode === 39) {
            moveRight()
        }
        if (e.keyCode === 40) {
            moveDown()
        }
    }
    document.addEventListener('keyup', control)


    function moveDown() {
        undraw()
        currentPosition += width
        draw()
        freeze()
    }

    function freeze() {
        if (currentTetromino.some(index => squares[currentPosition + index + width].classList.contains('taken'))) {
            currentTetromino.forEach(index => squares[currentPosition + index].classList.add('taken'))
            random = nextRandom
            nextRandom = Math.floor(Math.random()*Tetrominoes.length)
            currentTetromino = Tetrominoes[random][currentRotation]
            currentPosition = 4
            draw()
            displayShape()
            addScore()
            gameOver()
        }
    }

    function moveLeft() {
        undraw()
        const isAtLeftEdge = currentTetromino.some(index => (currentPosition + index) % width === 0)

        if (!isAtLeftEdge) currentPosition -= 1

        if (currentTetromino.some(index => squares[currentPosition + index].classList.contains('taken'))) {
            currentPosition += 1
        }
        draw()
    }
    
    function moveRight() {
        undraw()
        const isAtRightEdge = currentTetromino.some(index => (currentPosition + index) % width === width-1)

        if (!isAtRightEdge) currentPosition += 1

        if (currentTetromino.some(index => squares[currentPosition + index].classList.contains('taken'))) {
            currentPosition -= 1
        }
        draw()
    }

    function rotate() {
        undraw()
        currentRotation = (currentRotation + 1) % 4
        currentTetromino = Tetrominoes[random][currentRotation]
        draw()
    }

    const displaySquares = document.querySelectorAll('.mini-grid div')
    const displayWidth = 4
    const displayIndex = 0

    const upNextTetrominoes = [
        [1, displayWidth+1, displayWidth*2+1, 2], //L
        [0, displayWidth, displayWidth+1, displayWidth*2+1], //Z
        [1, displayWidth, displayWidth+1, displayWidth+2], //T
        [0, 1, displayWidth, displayWidth+1], //O
        [1, displayWidth+1, displayWidth*2+1, displayWidth*3+1]//I
    ]

    function displayShape() {
        displaySquares.forEach(square => {
            square.classList.remove('tetromino')
            square.style.backgroundColor = ''
        })
        upNextTetrominoes[nextRandom].forEach(index => {
            displaySquares[displayIndex + index].classList.add('tetromino')
            displaySquares[displayIndex + index].style.backgroundColor = colors[nextRandom]
        })
    }

    startBtn.addEventListener('click', () => {
        if (timerId) {
            clearInterval(timerId)
            timerId = null
        } else {
            draw()
            timerId = setInterval(moveDown, 500)
            nextRandom = Math.floor(Math.random()*Tetrominoes.length)
            displayShape()
        }
    })

    function addScore() {
        for (let i=0; i < 199; i+=width) {
            const row = [i, i+1, i+2, i+3, i+4, i+5, i+6, i+7, i+8, i+9]

            if (row.every(index => squares[index].classList.contains('taken'))) {
                score += 10
                scoreDisplay.innerHTML = score
                row.forEach(index => {
                    squares[index].classList.remove('taken')
                    squares[index].classList.remove('tetromino')
                    squares[index].style.backgroundColor = ''
                })
                const squaresRemoved = squares.splice(i, width)
                squares = squaresRemoved.concat(squares)
                squares.forEach(cell => grid.appendChild(cell))
            }
        }
    }

    function gameOver() {
        if (currentTetromino.some(index => squares[currentPosition + index].classList.contains('taken'))) {
            scoreDisplay.innerHTML = 'end'
            clearInterval(timerId)
        }
    }















})