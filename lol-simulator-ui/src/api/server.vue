<script>

import { http } from '../core/network/http.js'

function isUp () {
  return http.get('/status/is_up')
}

function getChampions () {
  return http.get('/riot/champions')
}

function getItems () {
  return http.get('/riot/items')
}
function getItemsCdragon () {
  return http.get('/cdragon/items')
}

function getCdn () {
  return http.get('/riot/cdn')
}

export default {
  isUp,
  getChampions,
  getItems,
  getItemsCdragon,
  getCdn
}

</script>
