import './style.css'

import { AxesHelper, BoxBufferGeometry, Float32BufferAttribute, Mesh, MeshNormalMaterial, BufferGeometry, PerspectiveCamera, Points, PointsMaterial, Scene, WebGLRenderer, MathUtils, TextureLoader, Group, Clock, LineBasicMaterial, Line, SphereBufferGeometry, ObjectLoader, CircleGeometry, AmbientLight } from "three";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader'
import { PointLight } from 'three';

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const scene = new Scene()//

const camera = new PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.01, 1000)//
camera.position.z = 1.5//
camera.position.y = 0.5//
camera.position.x = 0.3//
scene.add(camera)//

const count = 50//
const distance = 5//
const positions = new Float32Array(count * 3)//
const textureLoader = new TextureLoader()

var texturesPath = [
  "green_circle.png",
  "red_circle.png",
  "orange_circle.png",
  "purple_circle.png",
  "blue_circle.png",
  "bluegreen_circle.png"
]
// "/baptiste.jpg",
// "/emile.jpg",
// "/kilian.jpg",
// "/nathaniael.jpg",
var texturesCircles = []

for (var i = 0; i < texturesPath.length; i++) {
  var texture = textureLoader.load(texturesPath[i])
  texturesCircles.push(texture)
}

const group = new Group()

function addPoint(scene, positions, distance, circleTextureIndex, group) {
  for (let i = 0; i < positions.length; i++) {//
    positions[i] = MathUtils.randFloatSpread(distance)//
  }//
  const geometry = new BufferGeometry()
  geometry.setAttribute('position', new Float32BufferAttribute(positions, 3))
  const pointMaterial = new PointsMaterial({
    size: 0.1,
    alphaTest: 0.01,
    transparent: true,
    map: texturesCircles[circleTextureIndex]
  })
  
  const pointsObject = new Points(geometry, pointMaterial)
  
  const lineMaterial = new LineBasicMaterial({
    color: 0xffffff,
    linewidth: 1,
    transparent: true,
    opacity: 0.12,
    depthWrite: false
  })
  
  const lineObject = new Line(geometry, lineMaterial)

  group.add(lineObject)
  
  group.add(pointsObject)
}

// group.add(new Mesh(new SphereBufferGeometry(0.1, 32), new MeshNormalMaterial()))

let light = new PointLight(0xffffff, 2, 1000)
scene.add(light)

const gltfLoader = new GLTFLoader()

const panthere = gltfLoader.load( '/room.gltf', function ( gltf )
{
  const panthere = gltf.scene
  panthere.position.set(0, -0.3, 0)
  panthere.rotation.y = 1
  panthere.scale.set(0.5, 0.5, 0.5)
  group.add(panthere)
});

for (let i = 0; i < texturesCircles.length; i++) {
  addPoint(scene, positions, distance, i, group)
}

scene.add(group)

const renderer = new WebGLRenderer({
  antialias: true,
  alpha: true
})
renderer.clearColor(0x000000, 0)
renderer.setSize(window.innerWidth, window.innerHeight)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

const controls = new OrbitControls(camera, renderer.domElement)

document.body.appendChild(renderer.domElement)

const clock = new Clock()

let mouseX = 0
let mouseY = 0
let mouseControl = false

window.addEventListener('mousemove', (e) => {
  mouseX = e.clientX
  mouseY = e.clientY
})

window.addEventListener('click', (e) => {
  mouseControl = !mouseControl
})
function tick() {
  const time = clock.getElapsedTime()
  const ratioY = (mouseX / window.innerWidth - 0.5) * 2
  const ratioX = (mouseY / window.innerHeight - 0.5) * 2

  if (mouseControl) {
    group.rotation.x = 1 * ratioX * Math.PI
    group.rotation.y = 1 * ratioY * Math.PI
  } else {
    group.rotation.y = 0.1 * time
  }

  renderer.render(scene, camera)
  requestAnimationFrame(tick)
}

tick()

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight
  camera.updateProjectionMatrix()
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
})