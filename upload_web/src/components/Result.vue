<script setup>
import imageUrl from "@/assets/images/csv.png"; // => or relative path

const props = defineProps(["percent", "result", "fileName"]);
</script>

<template>
  <div v-if="percent >= 0 && percent < 100" class="progress-container">
    <img class="img" :src="imageUrl" alt="img" />
    <div class="input-percent-container">
      <div class="input-percent">
        <div>{{ fileName }}</div>
        <div>{{ percent }}%</div>
      </div>
      <progress id="file" :value="percent" max="100"></progress>
    </div>
  </div>

  <div v-if="percent == 100 && result" class="result-container">
    <div>Total {{ result.total }} Websites</div>
    <div class="time-text">(Use {{ result.process_time }} second)</div>
    <div class="box-container">
      <div class="up-site-box">
        <div class="title">Up</div>
        <div class="value">{{ result.up }}</div>
      </div>
      <div class="down-site-box">
        <div class="title">Down</div>
        <div class="value">{{ result.down }}</div>
      </div>
    </div>
  </div>
</template>

<style>
.progress-container {
  width: 656px;
  height: 140px;

  background: #ffffff;
  box-shadow: 0px 4px 30px 4px rgba(0, 0, 0, 0.1);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 31px 21px;
}

.progress-bar {
  width: 270px;
  height: 30px;
  left: 507px;
  top: 721px;

  background: #6749f5;
  border-radius: 21px;
}

.input-percent {
  display: flex;
  justify-content: space-between;
}

.img {
  width: 80px;
  height: 80px;
}

.input-percent-container {
  width: calc(100% - 80px);
}

progress {
  border-radius: 7px;
  width: 100%;
  height: 22px;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
}

progress::-webkit-progress-bar {
  background-color: rgb(254, 254, 254);
  border-radius: 21px;
}

progress::-webkit-progress-value {
  background: #6749f5;
  border-radius: 21px;
}

progress::-moz-progress-bar {
  /* style rules */
}

.result-container {
  width: 656px;
  height: 347px;
  padding: 40px 40px;

  background: #ffffff;
  box-shadow: 0px 4px 30px 4px rgba(0, 0, 0, 0.1);
  border-radius: 16px;
}

.up-site-box {
  width: 151px;
  height: 151px;

  background: #3fe364;
  border-radius: 16px;
  padding: 15px;

  font-family: "Roboto";
  font-style: normal;
  font-weight: 600;

  color: #ffffff;
}

.down-site-box {
  width: 151px;
  height: 151px;

  background: #f5f7fc;
  border-radius: 16px;
  padding: 15px;

  font-family: "Roboto";
  font-style: normal;
  font-weight: 600;

  color: #64697f;
}

.box-container {
  display: flex;
  justify-content: space-around;
  padding: 40px 40px;
}

.title {
  font-size: 24px;
}

.value {
  text-align: center;
  font-size: 72px;
  line-height: 84px;
}

.time-text {
  font-size: 24px;
}
</style>
