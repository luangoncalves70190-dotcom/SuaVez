import { Module } from '@nestjs/common';
import { AiController } from './ai/ai.controller';
import { AiService } from './ai/ai.service';
import { AnalyticsController } from './analytics/analytics.controller';
import { HospitalsController } from './hospitals/hospitals.controller';
import { HospitalsService } from './hospitals/hospitals.service';
import { QueueController } from './queue/queue.controller';
import { QueueService } from './queue/queue.service';

@Module({
  controllers: [HospitalsController, QueueController, AiController, AnalyticsController],
  providers: [HospitalsService, QueueService, AiService],
})
export class AppModule {}
