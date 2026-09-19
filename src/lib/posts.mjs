import { getCollection } from 'astro:content';

export async function getPublishedPosts() {
  return (await getCollection('posts'))
    .filter((post) => !post.data.draft)
    .sort((a, b) => a.data.pubDate.localeCompare(b.data.pubDate) || a.id.localeCompare(b.id));
}

export function postUrl(post) {
  return `/posts/${post.id}/`;
}
