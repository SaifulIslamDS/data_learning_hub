import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return { rules: { userAgent: "*", allow: "/" }, sitemap: "https://datalearninghub.netlify.app/sitemap.xml", host: "https://datalearninghub.netlify.app" };
}
