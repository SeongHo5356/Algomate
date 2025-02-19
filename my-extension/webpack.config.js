const path = require('path');

module.exports = {
    mode: 'production',             // or 'development'
    entry: './src/content/index.js', // 메인 엔트리 포인트
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'index.bundle.js'    // 최종 결과물
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            }
        ]
    }
};
