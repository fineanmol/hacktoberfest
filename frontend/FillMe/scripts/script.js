const usedColors = new Map()
const availableColors = [
	'red',
	'green',
	'blue',
	'yellow',
	'cyan',
	'crimson',
	'black',
	'coral',
]

const availableColorsElements = [
	...document.querySelector('.queue-table tr').children,
].reverse()

const renderAvailableColors = () => {
	// availableColors.forEach((availableColor, availableColorIndex) => {
	// 	availableColorsElements[availableColorIndex].classList.add(availableColor)
	// })

	availableColorsElements.forEach(
		(availableColorElement, availableColorIndex) => {
			availableColorElement.className = ''
			if (availableColorIndex >= availableColors.length) return
			availableColorElement.classList.add(availableColors[availableColorIndex])
		}
	)
}

const handleClick = e => {
	e.stopPropagation()

	const circleClasses = [...e.target.classList]

	const isColorInclude = circleClasses.some(circleClass =>
		[...usedColors.keys()].includes(circleClass)
	)

	if (isColorInclude) {
		const includeColor = circleClasses.find(circleColor =>
			[...usedColors.keys()].find(color => color === circleColor)
		)

		e.target.classList.remove(includeColor)
		e.target.style.borderColor = ''

		usedColors.delete(includeColor)
		availableColors.push(includeColor)
		renderAvailableColors()

		return
	}

	if (availableColors.length === 0) return
	e.target.classList.add(availableColors[0])
	e.target.style.borderColor = 'transparent'

	const removedColor = availableColors.shift()
	usedColors.set(removedColor, removedColor)
	renderAvailableColors()
}

const render = () => {
	const circleContainer = document.querySelector('[data-circle-container]')

	const circles = 8
	let createdCircle = 0

	while (createdCircle < circles) {
		const circleElement = document.createElement('div')
		circleElement.classList.add('circle', `circle${createdCircle + 1}`)
		circleContainer.append(circleElement)

		circleElement.addEventListener('click', handleClick)
		createdCircle++
	}

	renderAvailableColors()
}

onload = () => render()
