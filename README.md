# 个人博客

基于 Astro 的静态博客，准备发布到 `https://w0dex1nha01eng.github.io/`。文章使用 Markdown，页面由 GitHub Actions 自动构建。

## 本地预览

需要 Node.js 24 或更新版本。在此目录运行：

```bash
npm install
npm run dev
```

打开命令行显示的本地地址。正式构建使用 `npm run build`。

## 写新文章

在 `src/content/posts/` 新建一个 `.md` 文件。文件名会成为网址，例如 `weekend.md` 对应 `/posts/weekend/`。

```md
---
title: "文章标题"
description: "用一句话介绍这篇文章。"
pubDate: "2026-09-19"
---

从这里开始写正文。支持 **Markdown**。
```

首页会自动按 `pubDate` 从新到旧排列文章；文章底部的“上一篇／下一篇”也按日期连接。需要暂时隐藏文章时，在头部加 `draft: true`。发布前请替换或删除示例文章 `src/content/posts/first-note.md`。

站名、简介和导航在 `src/layouts/BaseLayout.astro`；Home 在 `src/pages/index.astro`，纯列表 Blog 在 `src/pages/blog.astro`，关于页在 `src/pages/about.astro`。

## 发布到 GitHub Pages

1. 在 GitHub 创建**公开**仓库 `w0dex1nha01eng.github.io`，不要勾选 README 或其他初始化文件。
2. 在本目录运行：

   ```bash
   git push -u origin main
   ```

3. 在仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
4. 等待仓库的 **Actions** 页面显示部署完成，访问 `https://w0dex1nha01eng.github.io/`。

以后修改文章并推送到 `main`，会自动重新发布。
