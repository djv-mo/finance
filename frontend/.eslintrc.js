module.exports = {
  env: {
    browser: true,
  },
  extends: "plugin:vue/vue3-essential",
  overrides: [
    {
      env: {
        node: true,
      },
      files: [".eslintrc.{js,cjs}"],
      parserOptions: {
        sourceType: "script",
      },
    },
  ],
  parserOptions: {
    ecmaVersion: 6,
    sourceType: "module",
    ecmaFeatures: {
      modules: true,
    },
  },
  plugins: ["vue"],
  rules: { "vue/multi-word-component-names": "off" },
};
