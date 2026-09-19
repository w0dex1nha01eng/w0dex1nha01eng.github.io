import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
  loader: glob({ base: './src/content/posts', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    draft: z.boolean().optional(),
  }),
});

export const collections = { posts };
