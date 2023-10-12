<template>
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" @click="openModal">
      Launch modal
    </button>

    <!-- Modal -->
    <div v-if="isOpen">
      {{ modalTitle }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false
    };
  },
  props: {
    modalTitle: {
      type: String,
      required: true
    }
  },
  methods: {
    openModal() {
      this.isOpen = true;
    },
    closeModal() {
      this.isOpen = false;
    }
  }
};
</script>