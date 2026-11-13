import 'dotenv/config';
import 'reflect-metadata';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const configuredOrigins = (process.env.CORS_ORIGINS || '')
    .split(',')
    .map(origin => origin.trim())
    .filter(Boolean);
  app.enableCors({ origin: configuredOrigins.length ? configuredOrigins : true });
  const port = Number(process.env.PORT || 3001);
  await app.listen(port);
  console.log(`SuaVez API disponível na porta ${port}`);
}
bootstrap();
