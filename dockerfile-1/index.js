const args = process.argv.slice(2)

const checkAge = async (arg) => {
    if (Number.isNaN(parseInt(arg))) return console.log('Second argument needs to be a number')
    const responseString = arg < 18 ? 'Is not over 18' : 'Is over 18'
    console.log(responseString)
}

const startClock = async (arg) => {
    if (arg && Number.isNaN(parseInt(arg))) return console.log('Second argument needs to be a number')
    let time = arg ? parseInt(arg) : 0
    const logTime = () => {
        console.log(++time)
        setTimeout(logTime, 1000)
    }
    logTime()
}

const drawTriangle = async (arg) => {
    if (Number.isNaN(parseInt(arg))) return console.log('Second argument needs to be a number')
    const height = parseInt(arg)
    let tree = ''
    for (let index = 0; index <= height; index++) {
        for (let index2 = 0; index2 < index; index2++) {
            if (index2 === 0 || index2 === index - 1 || index === height) {
                tree += '*'
            } else {
                tree += ' '
            }
        }
        tree += "\n"
    }
    console.log(tree)
}

const FEATURES = [
    {
        inputs: ['-a', '--adult'],
        function: checkAge
    },
    {
        inputs: ['-c', '--clock'],
        function: startClock
    },
    {
        inputs: ['-t', '--triangle'],
        function: drawTriangle
    }
]

const possible_inputs = FEATURES.map(f => f.inputs).reduce((acc, cur) => [...acc, ...cur], [])

if (args.length === 0 || !possible_inputs.includes(args[0])) {
    console.log(`
-h,       \t--help           \tto show this message
-a [age], \t--adult [age]    \tto check if you're older than 18
-c [time],\t--clock [time]   \tto start a clock
-t [size],\t--triangle [size]\tto draw a triangle, takes second argument as the size
    `)
    process.exit(0)
}

FEATURES.find(f => f.inputs.includes(args[0])).function(args[1])

process.on('SIGTERM', () => process.exit(0))
process.on('SIGINT', () => process.exit(0))
