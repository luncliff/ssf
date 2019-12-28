
// https://limdongjin.github.io/vuejs/vuepress/#기본적인-설정파일-vuepress-config-js

module.exports = {
    title: 'luncliff/ssf',
    description: 'Minimal C++ code snippet to build something',

    // redirect to: https://luncliff.github.io/ssf/...
    base: '/ssf',

    themeConfig: {
        repo: 'luncliff/ssf',
        repoLabel: 'GitHub',

        nav: [
          { text: 'Home', link: '/' },
          { text: 'Functions', link: '/functions' }
        ],
        sidebar: [
            {
                title: 'Modules',
                // path: '/foo/',      // optional, which should be a absolute path.
                sidebarDepth: 1,
                children: [
                    '/group__system',
                    '/group__socket'
                ]
            },
        ]
    },
    plugins: ['@vuepress/back-to-top']
}
