<script setup>
import UploadCSVVue from "./components/UploadCSV.vue";
import ResultVue from "./components/Result.vue";
import { ref } from "vue";

const apiURL = import.meta.env.VITE_API_URL;
const wsURL = import.meta.env.VITE_WS_URL;

const ws = ref(undefined);
const percent = ref();
const result = ref({});
const fileName = ref("input.csv");

async function uploadChange(event) {
  const files = event.target.files;
  if (event.target.files && event.target.files.length) {
    const file = files[0];
    fileName.value = file.name;
    const formData = new FormData();
    formData.append("file", file);
    const response = await fetch(apiURL + "/upload", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    if (response.status != 200) {
      alert(data.detail);
      return;
    } else {
      // Create WebSocket connection.
      const urlSocket = wsURL + "/upload/status/" + data.task_id;
      ws.value = new WebSocket(urlSocket);

      // Connection opened
      ws.value.addEventListener("open", (event) => {});

      // Listen for messages
      ws.value.addEventListener("message", (event) => {
        const { percent: percentData, result: resultData } = JSON.parse(
          event.data
        );
        if (percentData) {
          percent.value = percentData;
        }
        if (resultData) {
          result.value = resultData;
        }
      });
    }
  }
}
</script>

<template>
  <UploadCSVVue @fileChange="uploadChange" />
  <ResultVue :percent="percent" :result="result" :fileName="fileName" />
</template>

<style></style>
