module.exports = {
  lintOnSave: false,
  devServer: {
    public: "0.0.0.0:8080",
    proxy: {
      "^/api": {
        target: "http://localhost:5000",
        ws: true,
        changeOrigin: true,
      },
    },
  },
};
