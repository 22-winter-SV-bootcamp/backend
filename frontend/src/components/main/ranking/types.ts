export interface ImageInfo {
  url: string;
  count: number;
}

export type ImageType = "firstImage" | "secondImage";

export type ImageState = Record<ImageType, ImageInfo>;