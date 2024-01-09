import { PlayerFields } from "@/types/player_fields";

export interface Player {
  model: string;
  pk: number;
  fields: PlayerFields;
}
