import type { MetadataRoute } from "next";
import { getRouteManifest } from "@/src/lib/page-data";

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date("2026-08-05T00:00:00.000Z");
  const routes = Object.keys(getRouteManifest()).filter((route) => route !== "/404/");
  return [...routes, "/offline/"].map((route) => ({
    url: `https://datalearninghub.netlify.app${route}`,
    lastModified: now,
    changeFrequency: route === "/" ? "weekly" : "monthly",
    priority: route === "/" ? 1 : route.startsWith("/tutorials/") ? 0.8 : 0.6,
  }));
}
