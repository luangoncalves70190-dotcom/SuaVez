import { Controller, Get } from '@nestjs/common';

@Controller('api/analytics')
export class AnalyticsController {
  @Get() get() {
    return {
      today: 1284,
      waiting: 87,
      avgWait: 24,
      abandonmentRate: 3.2,
      aiInteractions: 391,
      completed: 1108,
      hourly: [28,41,63,74,91,112,103,86,69,52],
      labels: ['08h','09h','10h','11h','12h','13h','14h','15h','16h','17h']
    };
  }
}
