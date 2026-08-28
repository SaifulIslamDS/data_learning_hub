import type { MetadataRoute } from "next";

export const dynamic = "force-static";

export default function manifest(): MetadataRoute.Manifest {
  return {
    id: "/",
    name: "Data Learning Hub",
    short_name: "Data Learning Hub",
    description: "Learn Data Analytics through direct tutorials, browser practice, workflows, exercises, and portfolio projects.",
    start_url: "/",
    scope: "/",
    display: "standalone",
    orientation: "any",
    background_color: "#f7f7fc",
    theme_color: "#6257e8",
    lang: "en",
    categories: ["education", "productivity"],
    icons: [
      { src: "/icons/icon-192.png", sizes: "192x192", type: "image/png", purpose: "any" },
      { src: "/icons/icon-512.png", sizes: "512x512", type: "image/png", purpose: "any" },
      { src: "/icons/maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
    shortcuts: [
      { name: "Tutorials", short_name: "Tutorials", url: "/tutorials/", icons: [{ src: "/icons/icon-192.png", sizes: "192x192" }] },
      { name: "Projects", short_name: "Projects", url: "/projects/", icons: [{ src: "/icons/icon-192.png", sizes: "192x192" }] },
      { name: "My Learning", short_name: "My Learning", url: "/my-learning/", icons: [{ src: "/icons/icon-192.png", sizes: "192x192" }] },
    ],
  };
}
