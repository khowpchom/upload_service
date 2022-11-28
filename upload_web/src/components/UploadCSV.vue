<script setup>
import imageUrl from "@/assets/images/csv.png"; // => or relative path
import { ref } from "vue";

const emit = defineEmits(["fileChange"]);
const browseRef = ref();

function fileChange(event) {
  emit("fileChange", event);
}

function browseClick() {
  browseRef.value.click();
}
</script>

<template>
  <div class="title-upload">Websites Checker</div>
  <div class="upload_container">
    <img :src="imageUrl" alt="img" />
    <div>Drag your .csv file here to start uploading.</div>
    <div class="or-container">
      <div class="line"></div>
      OR
      <div class="line"></div>
    </div>

    <button class="browse-button" @click="browseClick">Browse File</button>
    <input v-show="false" ref="browseRef" type="file" @change="fileChange" />
  </div>
</template>

<style>
.upload_container {
  box-sizing: border-box;

  width: 656px;
  height: 405px;

  background: #f5f7fc;
  border: 4px dashed #c7cddb;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1.75rem;
}

.or-container {
  display: flex;
  gap: 14px;
  align-items: center;
}

.line {
  width: 112px;
  height: 0px;

  border: 3px solid #b6bed0;
}

.title-upload {
  width: 259px;
  height: 38px;
}
</style>
