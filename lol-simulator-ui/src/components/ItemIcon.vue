<template>
  <img class="item-picto"
        :src="link"
        @click="selected"/>
</template>

<script>

export default {
  name: 'ItemIcon',
  props: ['link', 'item'],
  data () {
    return {
    }
  },
  methods: {
    selected: function () {
      this.$emit('on-clicked', this.item)
    }
  },
  mounted: function () {
  },
  components: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img{
  margin: 5px;
  opacity: 0.6;
}
img:hover {
  height: 60px;
  opacity: 1;
  width: auto;
  margin: 0px;
  border: solid 6px #0077CC;
  border-radius: 10px;
}
</style>
