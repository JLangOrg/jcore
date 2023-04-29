function store(input){
  parts = input.split(' ')
  localstorage.setItem(parts[0], parts[2])
}
function get(input){
  return localstorage.getItem(input)
}
function log(input){
  console.log(input)
}
